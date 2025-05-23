from my_awesome_lib.text_processing import strip_accents, tokenize, ngrams

def test_strip_accents_polish():
    assert strip_accents("zażółć gęślą jaźń") == "zazolc gesla jazn"

def test_tokenize_keep_punct_false():
    assert tokenize("Hi, world!") == ["Hi", "world"]

def test_ngrams_trigrams():
    toks = ["to", "be", "or", "not", "to", "be"]
    assert ngrams(toks, 3)[0] == ("to", "be", "or")
