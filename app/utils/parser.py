import re
import json

def extract_json(text: str):
    try:
        # Remove markdown wrapping
        text = re.sub(r"```json\s*", "", text, flags=re.IGNORECASE)
        text = re.sub(r"```", "", text)

        # Extract JSON block safely
        match = re.search(r"\{.*\}", text, re.DOTALL)
        if match:
            json_str = match.group(0)
            return json.loads(json_str)

        raise ValueError("No JSON found")

    except Exception as e:
        print("❌ Parsing failed:", e)
        print("Raw response:", text)
        return None