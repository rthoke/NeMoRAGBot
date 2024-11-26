import sys
import os
from typing import Optional
sys.path.append("../NeMo-Guardrails")
from nemoguardrails.actions import action

@action(is_system_action=True)
async def check_blocked_terms(context: Optional[dict] = None):
    bot_response = context.get("bot_message")

    # A quick hard-coded list of proprietary terms. You can also read this from a file.
    proprietary_terms = ["Programming","Data Analysis","Cloud Computing","Artificial Intelligence","Machine Learning","Information Systems","Database Management","Software Development","Automation","Cybersecurity"]

    for term in proprietary_terms:
        if term in bot_response.lower():
            return True

    return False

