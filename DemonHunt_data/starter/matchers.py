"""Explicit character matchers; shifts are zero-based, including overlaps.
Counts exclude preprocessing; FA counts table lookups instead of comparisons.
Empty patterns match every boundary in whole-text matchers.
"""


def naive_match(T, P):
    shifts, comparisons = [], 0
    for s in range(len(T) - len(P) + 1):
        for j in range(len(P)):
            comparisons += 1
            if T[s + j] != P[j]:
                break
        else:
            shifts.append(s)
    return shifts, comparisons


def rabin_karp_match(T, P, d=256, q=101):
    if q <= 0:
        raise ValueError('modulus must be positive')
    n, m = len(T), len(P)
    if m == 0:
        return list(range(n + 1)), 0, 0
    if m > n:
        return [], 0, 0
    h = pow(d, m - 1, q)
    p = t = 0
    for j in range(m):
        p = (d * p + ord(P[j])) % q
        t = (d * t + ord(T[j])) % q
    shifts, comparisons, spurious = [], 0, 0
    for s in range(n - m + 1):
        if p == t:
            for j in range(m):
                comparisons += 1
                if T[s + j] != P[j]:
                    spurious += 1
                    break
            else:
                shifts.append(s)
        if s < n - m:
            t = (d * (t - ord(T[s]) * h) + ord(T[s + m])) % q
    return shifts, comparisons, spurious


def compute_prefix_function(P):
    pi = [0] * len(P)
    k = 0
    for i in range(1, len(P)):
        while k and P[k] != P[i]:
            k = pi[k - 1]
        if P[k] == P[i]:
            k += 1
        pi[i] = k
    return pi


def kmp_resume(T, P, pi, q, offset):
    if not P:
        return 0, list(range(offset, offset + len(T) + 1)), 0
    shifts, comparisons = [], 0
    for i, ch in enumerate(T):
        while True:
            comparisons += 1
            if ch == P[q]:
                q += 1
                break
            if q == 0:
                break
            q = pi[q - 1]
        if q == len(P):
            shifts.append(offset + i - len(P) + 1)
            q = pi[q - 1]
    return q, shifts, comparisons


def kmp_match(T, P):
    _, shifts, comparisons = kmp_resume(T, P, compute_prefix_function(P), 0, 0)
    return shifts, comparisons


def compute_transition_function(P, alphabet):
    # Fallback rows are already built, including the accepting state's row.
    alphabet = tuple(alphabet)
    pi = compute_prefix_function(P)
    delta = []
    for state in range(len(P) + 1):
        row = {}
        for ch in alphabet:
            if state < len(P) and P[state] == ch:
                row[ch] = state + 1
            elif state:
                row[ch] = delta[pi[state - 1]][ch]
            else:
                row[ch] = 0
        delta.append(row)
    return delta


def fa_match(T, delta, m):
    state = 0
    shifts = [0] if m == 0 else []
    for i, ch in enumerate(T):
        state = delta[state].get(ch, 0)
        if state == m:
            shifts.append(i - m + 1)
    return shifts, len(T)
