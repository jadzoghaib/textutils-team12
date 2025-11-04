import textutils.core as c

def test_slugify_basic():
    assert c.slugify("Hello World!") == "hello-world"
    assert c.slugify("multiple   spaces") == "multiple-spaces"

def test_slugify_accents_and_symbols():
    assert c.slugify("Café au lait") == "cafe-au-lait"
    assert c.slugify("Python&AI—2025") == "python-ai-2025"
    assert c.slugify("  -- already__slug-- ") == "already-slug"

