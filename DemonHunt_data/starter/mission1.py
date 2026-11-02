"""Mission 1: streaming KMP, with at most 4096 characters read at once."""
from pathlib import Path
from matchers import compute_prefix_function, kmp_resume
from utils import read_chunks

FILE = Path(__file__).resolve().parent.parent / 'data/crow_log.txt'
ALARM = 'KAKAKA'

def main():
    pi = compute_prefix_function(ALARM)
    print('pi =', pi)
    q = offset = count = 0
    first = []
    for chunk in read_chunks(FILE, 4096):
        q, shifts, _ = kmp_resume(chunk, ALARM, pi, q, offset)
        count += len(shifts)
        first.extend(shifts[:max(0, 10 - len(first))])
        offset += len(chunk)
    print('Alarm count:', count)
    print('First 10 shifts:', first)

if __name__ == '__main__':
    main()
