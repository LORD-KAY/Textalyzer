import unittest

from textalyzer.Textalyzer import (
    ContractionReplacers,
    RepeatingReplacers,
)


class FakeWordNet(object):
    def synsets(self, word):
        return [word] if word == "hello" else []


class ContractionReplacersTests(unittest.TestCase):
    def test_replaces_contractions(self):
        replacer = ContractionReplacers()

        self.assertEqual(
            replacer.text_replacers("I can't wait because it's late"),
            "I cannot wait because it is late",
        )

    def test_accepts_pattern_generator(self):
        patterns = ((pattern, replacement) for pattern, replacement in [(r"foo", "bar")])

        self.assertEqual(ContractionReplacers(patterns).text_replacers("foo"), "bar")


class RepeatingReplacersTests(unittest.TestCase):
    def test_stops_when_word_is_recognized(self):
        replacer = RepeatingReplacers(corpus=FakeWordNet())

        self.assertEqual(replacer.text_repeaters("helloooooooooooo"), "hello")

    def test_returns_unchanged_word_without_repeated_characters(self):
        replacer = RepeatingReplacers(corpus=FakeWordNet())

        self.assertEqual(replacer.text_repeaters("text"), "text")


if __name__ == "__main__":
    unittest.main()
