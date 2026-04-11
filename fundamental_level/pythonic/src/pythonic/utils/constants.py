import re

NAME_PATTERN: re.Pattern[str] = re.compile(r"[^a-zA-Z\x2D]")
