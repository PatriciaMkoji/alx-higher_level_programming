#!/usr/bin/python3
""" module test doc """

import unittest
import pep8
import inspect


class TestCodeFormat(unittest.TestCase):
    """ inherits from unittest """

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        mode_base = pep8style.check_files(['models/base.py',
                                           'models/rectangle.py',
                                           ])
        self.assertEqual(mode_base.total_errors, 0,
                         "Found code style errors (models_base).")
