import unittest
import logging
from homework_10 import log_event

class TestLogEvent(unittest.TestCase):

    def test_log_success(self):
        with self.assertLogs('log_event', level='INFO') as cm:
            log_event("alice", "success")

        self.assertEqual(cm.output, ["INFO:log_event:Login event - Username: alice, Status: success"])

    def test_log_expired(self):
        with self.assertLogs('log_event', level='WARNING') as cm:
            log_event("bob", "expired")

        self.assertIn("WARNING:log_event:Login event - Username: bob, Status: expired", cm.output)

    def test_log_failed(self):
        with self.assertLogs('log_event', level='ERROR') as cm:
            log_event("charlie", "failed")

        self.assertIn("ERROR:log_event:Login event - Username: charlie, Status: failed", cm.output)

    def test_log_unexpected_status(self):

        with self.assertLogs('log_event', level='ERROR') as cm:
            log_event("guest", "unknown_status")

        self.assertIn("ERROR:log_event:Login event - Username: guest, Status: unknown_status", cm.output)


if __name__ == '__main__':
    unittest.main()