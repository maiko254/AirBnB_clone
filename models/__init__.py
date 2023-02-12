#!/usr/bin/env python3
# __init__.py
# Mchael O Bonyo
"""Initializes the module models"""


from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
