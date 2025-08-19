import re
from datetime import datetime
from typing import Optional, Dict

LOG_RE = re.compile(
    r'^(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\s+'
    r'(?P<level>INFO|ERROR|WARNING)\s+'
    r'(?P<message>.*)$'
)

class LogEntry:
    def __init__(self, timestamp: datetime, level: str, message: str, raw: str):
        self.timestamp = timestamp
        self.level = level
        self.message = message
        self.raw = raw

    def to_dict(self):
        return {
            'timestamp': self.timestamp.isoformat(),
            'level': self.level,
            'message': self.message,
            'raw': self.raw
        }

class LogParser:
    """Parsează fișiere log linie cu linie. Liniile invalide sunt returnate ca `None`."""
    def parse_line(self, line: str) -> Optional[LogEntry]:
        line = line.rstrip('\n')
        m = LOG_RE.match(line)
        if not m:
            return None
        ts = datetime.strptime(m.group('timestamp'), '%Y-%m-%d %H:%M:%S')
        return LogEntry(ts, m.group('level'), m.group('message'), line)

    def parse_file(self, path: str):
        with open(path, 'r', encoding='utf-8') as f:
            for i, line in enumerate(f, 1):
                entry = self.parse_line(line)
                yield i, line, entry
