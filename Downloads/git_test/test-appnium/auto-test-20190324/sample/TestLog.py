from utils.logger import logger
import unittest

logger = logger(logger="TestLog").getlog()
class TestLog(unittest.TestCase):
    def test_log(self):
        logger.info("test log ")

if __name__ == "__main__":
    unittest.main()

