from collections import Counter
from typing import List
import json
from parser import LogEntry

class LogAnalyzer:
    def __init__(self, entries: List[LogEntry]):
        self.entries = entries  # list of LogEntry
        self.counter = Counter(e.level for e in entries)

    def summary(self):
        total = len(self.entries)
        by_level = dict(self.counter)
        first = min(self.entries, key=lambda e: e.timestamp).timestamp.isoformat() if self.entries else None
        last = max(self.entries, key=lambda e: e.timestamp).timestamp.isoformat() if self.entries else None
        return {
            'total': total,
            'by_level': by_level,
            'first_timestamp': first,
            'last_timestamp': last
        }

    def filter_by_keyword(self, keyword: str):
        return [e for e in self.entries if keyword.lower() in e.message.lower()]

    def filter_by_date_range(self, start, end):
        return [e for e in self.entries if start <= e.timestamp <= end]

    def export_json(self, path):
        data = {'summary': self.summary(), 'entries': [e.to_dict() for e in self.entries]}
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)
