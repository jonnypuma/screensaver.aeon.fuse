import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from rotation import count_of, kinds_on, round_path, round_seconds


class Rounds(unittest.TestCase):
    def test_kinds(self):
        self.assertEqual(kinds_on({}), ['movies', 'tvshows', 'music', 'cinema', 'today', 'tomorrow'])
        self.assertEqual(kinds_on({'tvshows': False, 'cinema': False}), ['movies', 'music', 'today', 'tomorrow'])
        self.assertEqual(kinds_on(dict((k, False) for k in ('movies', 'tvshows', 'music', 'cinema', 'today', 'tomorrow'))), ['movies'])

    def test_count(self):
        self.assertEqual(count_of(10), 10)
        self.assertEqual(count_of(6), 6)
        self.assertEqual(count_of(25), 10)
        self.assertEqual(count_of(1), 3)
        self.assertEqual(count_of(0), 10)
        self.assertEqual(count_of(None), 10)

    def test_path(self):
        p = round_path({'music': False}, 8, 3)
        self.assertEqual(p, 'plugin://script.aeon.helper/?info=ssround&n=8&kinds=movies,tvshows,cinema,today,tomorrow&r=3')
        self.assertNotEqual(round_path({}, 10, 1), round_path({}, 10, 2))

    def test_seconds(self):
        self.assertEqual(round_seconds(7, 10), 70)
        self.assertEqual(round_seconds(0, 10), 100)
        self.assertEqual(round_seconds(None, 5), 50)


if __name__ == '__main__':
    unittest.main()
