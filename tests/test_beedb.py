# -*- coding: utf-8 -*-

import unittest

from beedb import BeeDB, BeeDBError

class TestBeeDB(unittest.TestCase):

    def test_connect(self):
        db = BeeDB('user', 'database')
        self.assertIsNotNone(db)

    def test_connect_error(self):
        with self.assertRaises(BeeDBError):
            BeeDB('unknown_user', 'unknown_database')

    def test_init_db(self):
        db = BeeDB('user', 'database')
        db.init()

    def test_save_data(self):
        db = BeeDB('user', 'database')
        id = db.save(('name1', 'value1'), ('name2', 'value2'))
        self.assertIsNotNone(id)
        self.assertEqual(id, 1) # only if mock is used

    def test_get_data(self):
        db = BeeDB('user', 'database')
        id = db.save(('name1', 'value1'), ('name2', 'value2'))
        db.get('id')

    def test_delete_data(self):
        db = BeeDB('user', 'database')
        db.delete('id')

    def test_search_data(self):
        db = BeeDB('user', 'database')
        db.search('search phrase')
