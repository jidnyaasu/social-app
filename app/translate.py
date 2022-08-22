import requests
from flask_babel import _
from app import app


def translate(text, source_lang, target_lang):
    if "TRANSLATOR_URL" not in app.config or \
            not app.config["TRANSLATOR_URL"]:
        return _("Error: the translation service is not configured.")
    url = app.config["TRANSLATOR_URL"]
    params = {
        "source_lang": source_lang,
        "target_lang": target_lang,
        "text": text
    }
    r = requests.post(url=url, params=params)
    if r.status_code != 200:
        return _("Error: the translation service failed.")
    translated_data = r.json()
    if translated_data["status"] == "error":
        return _("Error: the translation service failed.")
    return translated_data["translatedText"]
