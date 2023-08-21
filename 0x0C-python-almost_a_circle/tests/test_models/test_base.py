#!/usr/bin/env python3

"""
A module that test differents behaviors
of the Base class
"""
import unittest
import pep8
from models.base import Base

class TestModel(unittest.TestCase):

    def setUp(self) -> None:
        self.b0 = Base()
        self.b01 = Base()
        self.b02 = Base()
        self.b2 = Base(4)
        self.b3 = Base(12)
        self.b4 = Base(-1)
        self.b5 = Base(-12)


    def test_pep8_base(self):
        """
        Test that checks PEP8
        """
        syntax = pep8.StyleGuide(quit=True)
        check = syntax.check_files(['models/base.py'])
        self.assertEqual(
            check.total_errors, 0,
            "Found code style errors (and warnings)."
        )



    def test_base__positive_id(self):
        """
        Tests for normal positive base ids
        """
        self.assertEqual(self.b2.id, 4)
        self.assertEqual(self.b3.id, 12)

    def test_base__negative_id(self):
        """
        Tests for normal negative base ids
        """
        self.assertEqual(self.b4.id, -1)
        self.assertEqual(self.b5.id, -12)

    def test_base__default_id(self):
        """
        Tests for normal default base ids
        """
        self.assertEqual(self.b0.id, 1)
        self.assertEqual(self.b01.id, 2)
        self.assertEqual(self.b02.id, 3)


def main():
    unittest.main()


if __name__ == "__main__":
    main()