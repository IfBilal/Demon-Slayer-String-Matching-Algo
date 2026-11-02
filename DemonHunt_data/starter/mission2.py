"""Mission 2: search both DNA orientations with finite automata."""
from pathlib import Path
from matchers import compute_transition_function, fa_match
from utils import read_text
FOLDER = Path(__file__).resolve().parent.parent / 'data/blood_samples'
DEMON_MARKER = 'GATTACAGATTC'

def reverse_complement(s):
    complement = dict(A='T', T='A', C='G', G='C')
    return ''.join(complement[ch] for ch in reversed(s))

def main():
    reverse = reverse_complement(DEMON_MARKER)
    delta = compute_transition_function(DEMON_MARKER, 'ACGT')
    rev_delta = compute_transition_function(reverse, 'ACGT')
    print('Marker:', DEMON_MARKER, ' Reverse complement:', reverse)
    print('delta: state  A  C  G  T')
    for state, row in enumerate(delta):
        print(f'{state:12}', *(f'{row[ch]:2}' for ch in 'ACGT'))
    demons = []
    print('Shifts refer to the stored forward sequence for both strands.')
    for path in sorted(FOLDER.glob('*.txt')):
        text = read_text(path)
        forward, _ = fa_match(text, delta, len(DEMON_MARKER))
        backward, _ = fa_match(text, rev_delta, len(reverse))
        print(f'{path.name}: forward={len(forward)} {forward}; reverse={len(backward)} {backward}')
        if forward or backward:
            demons.append(path.name)
    print('Demon sample(s):', ', '.join(demons))

if __name__ == '__main__':
    main()
