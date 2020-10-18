'''
Database file
'''
import pymongo


class MongoDB(object):
    '''
    Base class for Mongo client
    '''
    def __init__(self, dbname):

        self._conn = pymongo.MongoClient("localhost", 27017)
        self._db = self._conn[dbname]

    def get_db(self):
        return self._db
