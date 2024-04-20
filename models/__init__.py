#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.DBStorage import DBStorage


storage = DBStorage()
storage.reload()
