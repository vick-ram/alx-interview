#!/usr/bin/python3
"""0-stats module"""
import sys
import signal


total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0


def print_stats():
    """Print the statistics collected so far."""
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


def signal_handler(sig, frame):
    """Handle the keyboard interruption (CTRL + C)."""
    print_stats()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) >= 9 and parts[5] == '"GET' and parts[6].startswith(
                '/projects/260') and parts[7] == 'HTTP/1.1"':
            try:
                status_code = int(parts[8])
                file_size = int(parts[9])
                if status_code in status_codes:
                    status_codes[status_code] += 1
                total_size += file_size
                line_count += 1
            except ValueError:
                continue

        if line_count == 10:
            print_stats()
            line_count = 0

except KeyboardInterrupt:
    print_stats()
    sys.exit(0)

print_stats()
