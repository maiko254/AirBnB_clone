#!/usr/bin/env python3
# test_file_storage.py
# Michael O Bonyo
"""Implements unit tests for class FileStorage"""

import unittest
from models.engine.file_storage import FileStorage


class Test_File_Storage(unittest.TestCase):

    def test_method_all(self):
        store = FileStorage()
        self.assertIsInstance(store.all(), dict)
