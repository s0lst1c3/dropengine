import sqlite3

import core.helpers.crypto
import string
from hashlib import sha256

class Database(object):

    def __init__(self):

        self.conn = sqlite3.connect('dropengine.db')

    def initialize(self):

        self.conn.execute(""" CREATE TABLE IF NOT EXISTS dropengine (
                                            id INTEGER PRIMARY KEY,
                                            implant_id text NOT NULL,
                                            remote_key text NOT NULL
                                        ); """)


    def add(self, remote_key):


        implant_id = core.helpers.crypto.random_string(keyspace=string.ascii_letters)
        
        item = (implant_id, remote_key)
        
        self.conn.execute('insert into dropengine (implant_id, remote_key) values (?,?)', item)

        self.conn.commit()

        return implant_id, remote_key 

    def clear(self):
        self.conn.execute('delete from * dropengine')
        self.conn.commit()

    def drop(self):
        self.conn.execute('drop table dropengine')
        self.conn.commit()

    def retrieve(self, implant_id):


        item = (implant_id,)
        cursor = self.conn.execute('select * from dropengine where implant_id LIKE (?)', item)

        data = cursor.fetchall()

        if len(data) == 0:
            return None

        remote_key = data[0][2]

        cursor = self.conn.execute('delete from dropengine where implant_id LIKE (?)', item)
        self.conn.commit()

        return remote_key

