# -*- coding: utf-8 -*-
import unittest
from pyfiles.trial2_multiply import Multiply
from unittest.mock import patch

class TestMultiply(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_plus(self):
        conf = {"a": "test1", "b": "test2"}

        a = 1
        b = 2
        expect = 3
        actual = Multiply(conf).plus(a,b)
        self.assertEqual(expect, actual)

    def test_multiply(self):
        conf = {"a": "test1", "b": "test2"}

        a = -1
        b = 2
        expect = -2
        actual = Multiply(conf).multiply(a,b)
        self.assertEqual(expect, actual)

    @patch("pyfiles.trial2_multiply.Multiply.multiply", return_value=4)
    @patch("pyfiles.trial2_multiply.Multiply.plus", return_value=3)
    def test_plus_multiply(self, mock_plus, mock_multiply):
        conf = {"a": "test1", "b": "test2"}

        a = 1
        b = 2
        expect = 12
        actual = Multiply(conf).plus_multiply(a,b)
        print("a")
        print("plus",mock_plus(1,2))
        print("multipy",mock_multiply(1,2))
        self.assertEqual(expect, actual)
        self.assertTrue(mock_plus.called)
        self.assertTrue(mock_multiply.called)

    @patch("pyfiles.trial2_multiply.Multiply.plus")
    def test_plus_multiply2(self, mock_plus):
        conf = {"a": "test1", "b": "test2"}

        def _plus(a,b):
            if a > 0:
                return a + b
            else:
                return 0
        mock_plus.side_effect  = _plus
        a = -2
        b = 3
        expect = 0
        actual = Multiply(conf).plus_multiply(a,b)
        print("a", actual)
        print("plus",mock_plus(-2,3))
        self.assertEqual(expect, actual)
        self.assertTrue(mock_plus.called)

    def test_execute(self):
        conf = {"a": 1, "b": 2}
        expect = 6
        actual = Multiply(conf).execute()
        self.assertEqual(expect, actual)