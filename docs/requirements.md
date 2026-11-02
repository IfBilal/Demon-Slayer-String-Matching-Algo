# Assignment 3 requirements and completion map

Source: Assignment3.pdf, both pages; full extracted text in assignment_extracted.txt.
Due: Sunday 8 November 2026, 11:59 PM. Python selected.

- [x] Four lecture algorithms implemented in starter/matchers.py without built-in substring search or regex. Zero-based shifts and overlapping matches.
- [x] Final Selection: all 24 supplied checks PASS (10 marks).
- [x] Mission 1 (30): KAKAKA prefix array, count, first ten shifts; 4096-character reads with persistent KMP q and absolute offset. Supplied crow file is ASCII, so these reads are also 4096 bytes. Only count and first ten shifts retained between chunks.
- [x] Mission 2 (30): print 13-state delta table for GATTACAGATTC over ACGT; scan all ten files for forward marker and its reverse complement; report strand counts and shifts, identify demon.
- [x] Mission 3 (30): lowercase, punctuation to spaces per starter instruction, collapse spaces; 40-character rolling windows, d=256, q=1,000,000,007; hash-to-list-of-shifts map; explicit character verification; union of covered report characters; percentages and descending ranking; two-line explanation of paraphrase undercounting.
- [x] Bonus (+10): all four algorithms on a*100000 vs a*99+b; comparisons (FA lookups) and elapsed time in one bar-chart figure; leaderboard and three explanatory lines.
- [x] Submission: 24i-3166_DemonHunt.zip with completed starter as src/ and a two-page mission_report.pdf containing output captures for all four missions and bonus chart. data/ included so scripts remain runnable after extraction.

Course rules: copied code receives zero; submissions checked for similarity. A ten-minute viva may require tracing pi and delta and explaining the implementation. Review and understand the solution before submission. No portal upload was performed.

Interpretations: copied characters are counted once even when windows overlap; report length means cleaned length. Reverse matches are offsets in the stored forward sequence. Comparison counts exclude preprocessing; all elapsed times include preprocessing. FA lookups are not character comparisons. RK's zero verification comparisons in the arena do not mean zero computation: rolling hashes still take linear time.
