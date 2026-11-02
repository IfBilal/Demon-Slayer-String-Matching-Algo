"""Mission 3: verified rolling hashes and union of copied character ranges."""
from pathlib import Path
import unicodedata
from utils import read_text
ROOT = Path(__file__).resolve().parent.parent / 'data'
K, D = 40, 256

def clean_text(t):
    return ' '.join(''.join(' ' if unicodedata.category(ch).startswith('P') else ch
                            for ch in t.lower()).split())

def windows(text, k, d, q):
    if len(text) < k:
        return
    value = 0
    high = pow(d, k - 1, q)
    for i in range(k):
        value = (value * d + ord(text[i])) % q
    yield 0, value
    for s in range(1, len(text) - k + 1):
        value = (d * (value - ord(text[s - 1]) * high) + ord(text[s + k - 1])) % q
        yield s, value

def copy_detect(manual, report, k=K, d=D, q=1_000_000_007):
    if k <= 0 or q <= 0:
        raise ValueError('window length and modulus must be positive')
    index = {}
    for s, value in windows(manual, k, d, q):
        index.setdefault(value, []).append(s)
    covered = bytearray(len(report))
    for s, value in windows(report, k, d, q):
        for start in index.get(value, []):
            for j in range(k):
                if manual[start + j] != report[s + j]:
                    break
            else:
                for j in range(s, s + k):
                    covered[j] = 1
                break
    return 100 * sum(covered) / len(report) if report else 0.0

def main():
    manual = clean_text(read_text(ROOT / 'hashira_manual.txt'))
    scores = [(path.stem.removeprefix('report_').title(),
               copy_detect(manual, clean_text(read_text(path))))
              for path in sorted((ROOT / 'trainee_reports').glob('*.txt'))]
    for rank, (name, score) in enumerate(sorted(scores, key=lambda item: (-item[1], item[0])), 1):
        print(f'{rank}. {name:8} {score:6.2f}%')
    print('Changing words breaks exact 40-character windows, leaving fewer verified matches.')
    print('The score measures verbatim coverage, so it underestimates paraphrased copying.')

if __name__ == '__main__':
    main()
