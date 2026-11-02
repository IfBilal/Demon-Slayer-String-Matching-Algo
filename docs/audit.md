# Independent instructor review

Reviewed both assignment pages, source, two-page report and submission archive.

- All 24 supplied checks pass.
- Independent review ran 2,000 random matcher cases (Unicode and forced collisions) and 1,000 coverage/collision cases.
- Independent oracles confirmed all mission results and every DNA transition.
- Required algorithms, streaming, strand searches, normalization, hash verification, coverage, rankings and bonus pass.
- Original drawn output panels were rejected by review. Replaced with actual GTK/VTE terminal window screenshots after running each mission, using capture_terminal.py; no recreated text panels remain.
- Explicit bonus winner rationale and Pillow>=10.1 dependency added.
- Page-one heading overlap corrected after screenshot replacement.
- Report remains two pages; zip includes src/, data/, report and bonus chart.

Reviewer found no computational defects. Assessment is not an instructor's official grade; viva and course similarity checks remain the student's responsibility.

To refresh terminal screenshots on this Linux desktop, run:

    python docs/capture_terminal.py mission1
    python docs/capture_terminal.py mission2
    python docs/capture_terminal.py mission3
    python docs/capture_terminal.py mission4
    python docs/build_report.py

Capture requires GTK 3, VTE 2.91, PyGObject and an X11 display. These are documentation-generation dependencies only; assignment scripts do not require them.
