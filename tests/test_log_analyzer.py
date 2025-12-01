import unittest
from src.modules.log_analyzer import LogAnalyzer

class TestLogAnalyzer(unittest.TestCase):

    def setUp(self):
        self.log_analyzer = LogAnalyzer()
        self.sample_logs = [
            "2023-10-01 12:00:00 INFO Sample log entry 1",
            "2023-10-01 12:05:00 ERROR Sample error entry 2",
            "2023-10-01 12:10:00 WARNING Sample warning entry 3",
        ]
        self.log_analyzer.load_logs(self.sample_logs)

    def test_load_logs(self):
        self.assertEqual(len(self.log_analyzer.logs), 3)

    def test_filter_by_keyword(self):
        filtered_logs = self.log_analyzer.filter_logs(keyword="ERROR")
        self.assertEqual(len(filtered_logs), 1)
        self.assertIn("ERROR Sample error entry 2", filtered_logs)

    def test_filter_by_date(self):
        filtered_logs = self.log_analyzer.filter_logs(date="2023-10-01")
        self.assertEqual(len(filtered_logs), 3)

    def test_display_logs(self):
        displayed_logs = self.log_analyzer.display_logs()
        self.assertTrue(isinstance(displayed_logs, list))
        self.assertGreater(len(displayed_logs), 0)

if __name__ == '__main__':
    unittest.main()