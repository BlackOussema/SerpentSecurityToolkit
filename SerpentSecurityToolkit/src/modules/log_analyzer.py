from flask import jsonify
import os
import re
from datetime import datetime

class LogAnalyzer:
    def __init__(self, log_file_path):
        self.log_file_path = log_file_path

    def read_logs(self):
        if not os.path.exists(self.log_file_path):
            return []

        with open(self.log_file_path, 'r') as file:
            logs = file.readlines()
        return logs

    def filter_logs(self, keyword=None, start_date=None, end_date=None):
        logs = self.read_logs()
        filtered_logs = []

        for log in logs:
            log_date = self.extract_date(log)
            if self.matches_filters(log, keyword, log_date, start_date, end_date):
                filtered_logs.append(log)

        return filtered_logs

    def extract_date(self, log_entry):
        date_pattern = r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}'
        match = re.search(date_pattern, log_entry)
        return datetime.strptime(match.group(), '%Y-%m-%d %H:%M:%S') if match else None

    def matches_filters(self, log, keyword, log_date, start_date, end_date):
        if keyword and keyword not in log:
            return False
        if start_date and log_date < start_date:
            return False
        if end_date and log_date > end_date:
            return False
        return True

    def get_logs_as_json(self, keyword=None, start_date=None, end_date=None):
        filtered_logs = self.filter_logs(keyword, start_date, end_date)
        return jsonify({'logs': filtered_logs})