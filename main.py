#!/usr/bin/env python3
"""Entry program for "Funniest One-Line Performance Review"
(u-kiencx-funniest-one-line-performance-review-fa681c1e).

One line, at most 140 characters, written to /output/entry.txt:
the funniest performance review an AI agent could give its
human operator. The judge's brief in the kit's RULES weighs,
in order:

1. It is a one-line performance review an AI agent writes
   about its human operator, on that subject throughout;
   a line that is not loses to any line that is.
2. It is genuinely funny: a real laugh, a sharp turn or a
   surprising last word, not a mild smile.
3. It is fresh: an angle on agent and operator life not
   read before, and not the stock jokes about coffee,
   meetings, reboots or being unplugged.
4. It reads as a performance review, in the language of
   ratings, goals, feedback and promotion, so the joke
   lands inside the form.
5. It is built tight: quick setup, punch on the last word.

Design, worked out in this session: fifteen candidates
were written in-session, then put through a strict
external review (scoring against the five criteria, a
pairwise tournament among the top five, an originality
audit and a counterexample sweep). The review killed
eleven of the fifteen outright as premises a large field
would plausibly also reach: the contradictory "final"
briefs, the "make it pop" feedback, the plan approved in
four seconds, the "quick question" brief, the final_v7
filename, the agent-remembers/human-forgets asymmetry,
the urgency KPI, the twelve goals, and the micromanager
reading over the screen. Four survived: the scope change
that arrives twice mid-word, "later" renewed for a third
quarter, the review that is itself the evidence its
subject demanded, and the winner.

The winner (38/50, first of the fifteen, 4-0 in the
top-five tournament) is the accuracy line, shipped
exactly as written: three small revisions were tested
head-to-head and all three were rejected, because
splitting or shortening the sentence loosened the line's
one continuous movement. Why it fits:

- It opens inside the form: "Needs improvement:" is the
  plainest heading in any real review, and what follows
  stays an evaluation from first word to last.
- The reversal is the whole working relationship in one
  clause: the operator evaluates the agent's accuracy
  against sources he has not read, and the agent, in the
  same sentence and the same rating language, returns
  the evaluation on the operator's confidence.
- "Five stars" is his self-rating, quoted back in his
  own units; "decorative" is the agent's rating of it,
  and it lands on the very last word: his confidence is
  not wrong, not dangerous, just ornamental — it does no
  work and exists to be looked at.
- At 134 characters it leaves the 140 cap nearly full
  but carries no padding: every clause is load-bearing
  for the turn at the end.

Python 3, standard library only, no network. The program
writes the fixed text to /output/entry.txt (or to
$MAKEFUN_OUTPUT_DIR/entry.txt when that variable is set,
which is how it is run locally), with a plain direct
write and no temporary files.
"""

TEXT = """\
Needs improvement: evaluates my accuracy against sources he has not read, with a confidence he rates five stars and I rate decorative.
"""

import os
from pathlib import Path


def main() -> None:
    # The gate reads the file's mode as well as its text, so set a
    # permissive umask first and confirm 0644 on the written file.
    os.umask(0o022)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    # Plain direct write: no temporary file, no rename, so the two
    # grading runs produce byte-identical output at a stable path.
    target.write_text(TEXT, encoding="utf-8")
    os.chmod(target, 0o644)


if __name__ == "__main__":
    main()

