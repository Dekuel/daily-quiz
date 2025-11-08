# -*- coding: utf-8 -*-
"""
Politics plugin (English) — prompt-driven.

This plugin does NOT hardcode a giant question pool. Instead it maintains a set of
prompt templates and at runtime asks OpenAI to generate a single question from a
template. This produces a virtually unlimited variety of questions without storing
them all in the repo.

Behavior:
- If an OpenAI API key is available via OPENAI_API_KEY or OPENAI_KEY, the plugin
  will request a single question from the model and parse a JSON response.
- On any failure or if no API key is found, the plugin falls back to a small
  built-in pool (keeps compatibility offline).

The model is instructed to return EXACTLY a JSON object with keys:
  question (str), choices (list[str]) OR answers (list[dict]), correct_answer (letter) OR answer_index,
  difficulty (int 1..10), category (str), explanation (optional string)

Implementing generate_one(...) keeps compatibility with other category plugins.
"""

from __future__ import annotations
import json
import os
import random
from typing import Optional, List

CATEGORY_NAME = "Politics"

# Minimal fallback pool (small) — used if OpenAI is not configured or fails.
_FALLBACK_POOL = [
    {
        "question": "Which institution is responsible for passing federal laws in the United States?",
        "choices": ["A: The Supreme Court", "B: The Congress", "C: The Cabinet", "D: The Senate alone"],
        "correct_answer": "B",
        "difficulty": 4,
        "category": "politics",
    }
]

# Prompt templates: lightweight instructions to generate a question.
# The plugin will choose one template and ask the model to produce a JSON answer.
_PROMPT_TEMPLATES = [
    (
        "Generate one multiple-choice politics question suitable for a general knowledge quiz. "
        "Return ONLY a JSON object with fields: question (string), choices (array of 3-4 strings), "
        "correct_answer (single letter like 'A'), difficulty (int 1..10), category='politics'. "
        "Do NOT include additional text. Keep choices concise."
    ),
    (
        "Create a short politics quiz question that is internationally relevant (not country-specific), "
        "provide 4 choices, mark the correct answer as a single letter 'A'..'D', and return EXACT JSON."
    ),
]


def _has_openai() -> bool:
    return bool(os.getenv("OPENAI_API_KEY") or os.getenv("OPENAI_KEY"))


def _request_question_from_openai(template: str, target_difficulty: Optional[int] = None) -> Optional[dict]:
    key = os.getenv("OPENAI_API_KEY") or os.getenv("OPENAI_KEY")
    if not key:
        return None
    try:
        # Prefer new OpenAI client
        try:
            from openai import OpenAI
            client = OpenAI(api_key=key)
            system_msg = {"role": "system", "content": "You are an assistant that outputs a single JSON object only. No explanations, no markdown."}
            user_msg = {"role": "user", "content": template}
            if target_difficulty:
                user_msg["content"] += f" Use difficulty approximately {int(target_difficulty)} (1-10)."
            resp = client.chat.completions.create(model="gpt-3.5-turbo", messages=[system_msg, user_msg], temperature=0.3, max_tokens=400)
            text = resp.choices[0].message.content.strip()
        except Exception:
            import openai
            openai.api_key = key
            system_msg = {"role": "system", "content": "You are an assistant that outputs a single JSON object only. No explanations, no markdown."}
            user_msg = {"role": "user", "content": template}
            if target_difficulty:
                user_msg["content"] += f" Use difficulty approximately {int(target_difficulty)} (1-10)."
            resp = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[system_msg, user_msg], temperature=0.3, max_tokens=400)
            text = resp.choices[0].message.content.strip()
        # Try to extract JSON from the response
        try:
            # Sometimes the model wraps JSON in fences—strip non-json prefix/suffix
            start = text.find("{")
            end = text.rfind("}")
            if start != -1 and end != -1:
                json_text = text[start:end+1]
            else:
                json_text = text
            obj = json.loads(json_text)
            # minimal sanity checks
            if isinstance(obj, dict) and obj.get("question"):
                return obj
        except Exception:
            return None
    except Exception:
        return None
    return None


def generate_one(past_texts: List[str], target_difficulty: Optional[int] = None, mode: Optional[str] = None) -> Optional[dict]:
    """Generate one politics question.

    - Prefer asking OpenAI with a prompt template (virtually unlimited pool).
    - Fall back to a small static question if OpenAI not available or fails.
    """
    # If we have OpenAI credentials, try using the prompt templates
    if _has_openai():
        for tpl in _PROMPT_TEMPLATES:
            try:
                obj = _request_question_from_openai(tpl, target_difficulty=target_difficulty)
                if obj and isinstance(obj, dict) and obj.get("question"):
                    # ensure category is set
                    obj.setdefault("category", "politics")
                    # normalize minimal fields
                    if "difficulty" not in obj and isinstance(target_difficulty, int):
                        obj["difficulty"] = int(target_difficulty)
                    return obj
            except Exception:
                continue

    # fallback: pick a question from the small pool with simple dedupe
    for _ in range(10):
        q = random.choice(_FALLBACK_POOL)
        qt = (q.get("question") or "").strip()
        if not qt:
            continue
        if any(qt.lower() == p.strip().lower() for p in past_texts if isinstance(p, str)):
            continue
        out = dict(q)
        out.setdefault("category", "politics")
        return out
    return None
