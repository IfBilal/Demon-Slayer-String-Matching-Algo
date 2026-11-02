"""Independent exhaustive and collision/coverage regression checks."""
import itertools
import unittest
from matchers import *
from mission3 import copy_detect, clean_text

class RegressionTests(unittest.TestCase):
    def test_exhaustive_matchers_and_streaming(self):
        words = [''.join(w) for n in range(6) for w in itertools.product('ab', repeat=n)]
        for text in words:
            for pattern in words[:15]:
                expected = [s for s in range(len(text) - len(pattern) + 1) if text.startswith(pattern, s)]
                self.assertEqual(naive_match(text, pattern)[0], expected)
                self.assertEqual(rabin_karp_match(text, pattern, q=2)[0], expected)
                self.assertEqual(kmp_match(text, pattern)[0], expected)
                self.assertEqual(fa_match(text, compute_transition_function(pattern, 'ab'), len(pattern))[0], expected)
                if pattern:
                    for split in range(len(text) + 1):
                        pi = compute_prefix_function(pattern)
                        q, a, _ = kmp_resume(text[:split], pattern, pi, 0, 0)
                        _, b, _ = kmp_resume(text[split:], pattern, pi, q, split)
                        self.assertEqual(a + b, expected)

    def test_coverage_and_collisions(self):
        self.assertEqual(copy_detect('aaaa', 'aaaaa', k=3), 100)
        self.assertEqual(copy_detect('abc', 'xyz', k=3, q=1), 0)
        self.assertEqual(copy_detect('abc', 'abcXYZ', k=3), 50)
        self.assertEqual(copy_detect('abc', '', k=3), 0)
        self.assertEqual(clean_text(' HI,\nWorld!  '), 'hi world')

    def test_unknown_alphabet(self):
        self.assertEqual(fa_match('abXabab', compute_transition_function('ab', 'ab'), 2)[0], [0, 3, 5])

if __name__ == '__main__':
    unittest.main()
