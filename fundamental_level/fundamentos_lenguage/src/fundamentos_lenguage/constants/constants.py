import re

GENDER_SWAP: dict[str, str] = {"male": "hombre", "female": "mujer"}
LATIN_ALFABET: re.Pattern[str] = re.compile(r"[^a-zA-Z\s]")
