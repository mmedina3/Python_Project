#!/usr/bin/env python


def titleize(input_string):
    result = ""
    words = input_string.split()
    for idx, word in enumerate(words):
        words[idx] = word.capitalize()
    result = " ".join(words)
    return result




def test_capitalizes_a_word():
    assert titleize("jaws") == "Jaws"

def test_capitalizes_every_word_aka_title_case():
    assert titleize("david copperfield") == "David Copperfield"

# def test_doesnt_capitalize_little_words_in_a_title:
#     assert titleize("war and peace")).to eq("War and Peace")

# def test_does_capitalize_little_words_at_the_start_of_a_title:
#     assert titleize("the bridge over the river kwai")).to eq("The Bridge over the River Kwai")