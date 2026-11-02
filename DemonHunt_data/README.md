# Demon Slayer Corps — The String Hunt (starter pack)

    data/
      crow_log.txt          Mission 1: messages from the Kasugai crows (~5 MB)
      blood_samples/        Mission 2: 10 villagers' blood DNA, one sequence per file (~1 million bases each)
      hashira_manual.txt    Mission 3: the leaked Hashira Training Manual
      trainee_reports/      Mission 3: five trainee reports to check
    starter/
      matchers.py           YOUR FOUR TECHNIQUES GO HERE (fill the TODOs)
      test_matchers.py      Final Selection: every line must say PASS
      utils.py              ready-made helpers (chunk reader, file reader, timer)
      mission1.py .. mission3.py   one script per mission, with TODOs
      mission4.py           BONUS: Breathing Styles Tournament (optional)

## How to start
1. Install Python 3.10 or newer.
2. Open a terminal inside the `starter` folder.
3. Fill in `matchers.py` one function at a time, using the pseudocode from Lectures 7–9.
4. Run `python test_matchers.py` until every line says PASS.
5. Then complete `mission1.py` to `mission3.py` and run each one.
6. Want Hashira rank? Do the bonus in `mission4.py`.

Due: Sunday 8 November 2026, 11:59 PM.

Positions (shifts) start from 0. Do not use built-in search (find, in, count, re) inside your matchers.
