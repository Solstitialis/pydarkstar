import unittest

import pydarkstar.logutils
import pydarkstar.database
import pydarkstar.auction.manager
import pydarkstar.rc

pydarkstar.logutils.setDebug()

class TestCase(unittest.TestCase):
    def setUp(self):
        self.db = pydarkstar.database.Database.pymysql(**pydarkstar.rc.sql)
        self.ob = pydarkstar.auction.manager.Manager(self.db, fail=True)

    def test_init(self):
        pass

if __name__ == '__main__':
    unittest.main()