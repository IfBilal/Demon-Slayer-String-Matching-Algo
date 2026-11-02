"""Bonus arena. Pillow draws one chart with separate count/time scales."""
from pathlib import Path
from matchers import naive_match, rabin_karp_match, kmp_match, compute_transition_function, fa_match
from utils import Timer
ARENA = ('a' * 100_000, 'a' * 99 + 'b')

def main():
    from PIL import Image, ImageDraw, ImageFont
    T, P = ARENA
    results = []
    for name, matcher in [('Naive', naive_match), ('Rabin-Karp', rabin_karp_match), ('KMP', kmp_match), ('Automaton', None)]:
        with Timer() as timer:
            if matcher is None:
                delta = compute_transition_function(P, 'ab')
                shifts, count = fa_match(T, delta, len(P))
            else:
                shifts, count, *extra = matcher(T, P)
        assert shifts == []
        results.append((name, count, timer.seconds))
    print('Times include preprocessing; RK uses d=256, q=101.')
    print('Character comparisons; automaton reports table lookups instead.')
    for name, count, seconds in sorted(results, key=lambda row: row[2]):
        print(f'{name:12} {count:10,d} operations  {seconds:.6f} s')
    winner = min(results, key=lambda row: row[2])[0]
    print(f'{winner} wins this run; FA scans with one table lookup per character.')
    print('Naive loses: all 100 characters are compared at each of 99,901 shifts.')
    print('KMP reuses prefixes; FA uses one lookup per character; RK rejects hashes without verification.')
    image = Image.new('RGB', (1400, 650), 'white')
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default(size=20)
    draw.text((30, 15), 'Infinity Castle: 100,000 a characters vs. 99 a characters + b', fill='black', font=font)
    for panel, label, column in [(0, 'Comparisons / FA lookups (linear)', 1), (1, 'Elapsed seconds (linear, includes setup)', 2)]:
        x = 35 + panel * 700
        draw.text((x, 65), label, fill='black', font=font)
        maximum = max(row[column] for row in results)
        for i, row in enumerate(results):
            y = 130 + i * 115
            draw.text((x, y), row[0], fill='black', font=font)
            width = int(450 * row[column] / maximum)
            if width:
                draw.rectangle((x, y + 35, x + width, y + 62), fill='#276a9d')
            value = f'{row[column]:,}' if column == 1 else f'{row[column]:.6f}'
            draw.text((x + width + 8, y + 35), value, fill='black', font=font)
    out = Path(__file__).resolve().parent.parent / 'output'
    out.mkdir(exist_ok=True)
    image.save(out / 'bonus_chart.png')

if __name__ == '__main__':
    main()
