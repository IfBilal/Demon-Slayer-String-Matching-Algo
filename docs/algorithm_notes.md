# Implementation and viva notes

Naive tries every legal shift and stops on the first unequal character: O(nm) worst-case time.
Rabin–Karp updates a polynomial hash by removing the outgoing leading digit, multiplying by d and adding the incoming digit modulo q. Equal hashes only trigger verification, never establish a match. Worst-case O(nm), linear expected scan plus verification.
KMP pi[i] is the longest proper prefix ending at i. On mismatch q falls back to pi[q-1] without consuming the current text character. On a full match it also falls back, preserving overlap. KAKAKA has pi=[0,0,1,2,3,4]. Streaming state is q plus the absolute number of characters already read. O(n+m) time, O(m) auxiliary state excluding reported matches.
The automaton's state is the length of the longest pattern prefix that is a suffix of consumed text. A matching next character advances; otherwise the already-built fallback row supplies the transition. Even state m has outgoing transitions, so overlaps work. Construction O(m*alphabet size), scan O(n).
Mission 3 uses rolling hashes to index manual windows and checks candidate report windows character by character. Its byte mask forms the union of all verified report intervals. Heavy repetition or collisions can increase verification work; hash equality alone never counts as copying.

Inosuke's report rewrites manual passages. Exact 40-character matching cannot detect their meaning, so his 14.96% score is a measure of verbatim overlap rather than total borrowed ideas.

Verification: supplied 24 cases all PASS; exhaustive binary texts of lengths 0–5 and patterns of lengths 0–3 compared with an independent startswith oracle, including every streaming split for nonempty patterns. Deliberately small moduli test collisions; additional tests cover overlapping coverage, punctuation, empty reports and unknown alphabet symbols. Empty whole-text patterns match all boundaries; missions use nonempty patterns.
