#!/usr/bin/python3
"""
the __init__module
create a unique FileStorage instance for your application
"""


from engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()