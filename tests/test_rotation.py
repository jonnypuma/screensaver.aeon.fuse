import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from rotation import at, sections


class Rotation(unittest.TestCase):
    def test_all_on(self):
        self.assertEqual([k for k, _ in sections({}, {})], ['movies', 'tvshows', 'music'])

    def test_switched_off(self):
        self.assertEqual([k for k, _ in sections({'tvshows': False}, {})], ['movies', 'music'])

    def test_empty_library_skipped(self):
        self.assertEqual([k for k, _ in sections({}, {'music': 0, 'movies': 5, 'tvshows': None})], ['movies', 'tvshows'])

    def test_never_empty(self):
        self.assertEqual([k for k, _ in sections({'movies': False, 'tvshows': False, 'music': False}, {})], ['movies'])

    def test_cycle(self):
        seq = ['a', 'b', 'c']
        self.assertEqual([at(seq, 100, 100 + t, 60) for t in (0, 59, 60, 125, 180, 241)], ['a', 'a', 'b', 'c', 'a', 'b'])

    def test_bad_interval(self):
        self.assertEqual(at(['a', 'b'], 0, 3, 0), 'b')


if __name__ == '__main__':
    unittest.main()
