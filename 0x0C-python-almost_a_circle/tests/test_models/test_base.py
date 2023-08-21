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
        b1 = Base()
        b2 = Base(12)
        b3 = Base()



    def test_model_id(self):
        self.assertEqual(self.b1.id, 0)
        self.assertEqual(self.b2.id, 12)
        self.assertEqual(self.b3.id, 1)


def main():
    unittest.main()


if __name__ == "__main__":
    main()