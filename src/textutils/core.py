def test_normalise_whitespace_remove_extra_spaces():
    text = ' a b \n c '
    assert c.normalise_whitespace(text) == 'a b c'

