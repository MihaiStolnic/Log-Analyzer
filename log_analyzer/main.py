import argparse
from parser import LogParser
from analyzer import LogAnalyzer
from visualizer import Visualizer
from datetime import datetime
import sys

def main():
    p = argparse.ArgumentParser(description='Log File Analyzer')
    p.add_argument('path', help='Path to a .log file')
    p.add_argument('--export', help='Export results to JSON file')
    p.add_argument('--plot', action='store_true', help='Show a plot of counts per level')
    p.add_argument('--keyword', help='Filter entries by keyword')
    args = p.parse_args()

    parser = LogParser()
    entries = []
    invalid = []
    for lineno, raw_line, entry in parser.parse_file(args.path):
        if entry is None:
            invalid.append((lineno, raw_line))
        else:
            entries.append(entry)

    analyzer = LogAnalyzer(entries)
    summary = analyzer.summary()
    print('--- Summary ---')
    print(summary)
    print(f'Invalid lines: {len(invalid)}')
    if args.keyword:
        found = analyzer.filter_by_keyword(args.keyword)
        print(f'Entries matching "{args.keyword}": {len(found)}')

    if args.export:
        analyzer.export_json(args.export)
        print(f'Exported results to {args.export}')

    if args.plot:
        viz = Visualizer(entries)
        viz.plot_level_counts()

if __name__ == "__main__":
    main()
