# -*- coding: utf-8 -*-
import unittest
from pyfiles.trial1_plus import Plus

class TestTashizan(unittest.TestCase):
    """test class of trial1_plus.py
    """
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_tashizan1(self):
        """test method for tashizan
        """
        expects = {
            "trial1" : {"a": 1,  "b": 2,  "res":3},
            "trial2" : {"a": 1,  "b": 4,  "res":5},
            "trial3" : {"a": 1,  "b": -1,  "res":0},
        }
        for key in expects.keys():
            conf = {"a":expects[key]["a"], "b":expects[key]["b"]}
            plus = Plus(conf)
            actual = plus.execute()
            self.assertEqual(expects[key]["res"],actual)

    def test_tashizan2(self):
        """test method for tashizan
        """
        conf = {"a":-1, "b":1}
        expected = 0
        plus = Plus(conf)
        actual = plus.execute()
        self.assertEqual(expected, actual)
