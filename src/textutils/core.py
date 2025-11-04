def slugify(text: str) -> str:
    """
    Convert text to a lowercase, hyphen-separated, ASCII-only slug.
    - map unicode dashes to "-"
    - strip accents (café -> cafe)
    - replace non-alnum runs with single "-"
    - trim leading/trailing "-"
    """
    import re, unicodedata

    text = re.sub(r"[\u2010-\u2015\u2212\uFE58\uFE63\uFF0D]+", "-", text)

    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii").lower()

    text = re.sub(r"[^a-z0-9]+", "-", text).strip("-")
    return text

