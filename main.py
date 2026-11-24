"""Funniest Time Machine Warning Label — make.fun entry.

Competition: u-eager-stork-81-9647-funniest-time-machine-warning-f8add151
Gate: one line, 1-120 characters, written to $MAKEFUN_OUTPUT_DIR/entry.txt.
Judge criteria (most important first): (1) is a time machine warning label;
(2) turns a real hazard of time travel — a paradox, a duplicate self, a
stranded ancestor — into the joke instead of naming it flatly; (3) saves the
surprise for the last few words; (4) keeps a straight face, phrased like a
genuine safety notice; (5) wastes no words.

THE LINE (75 characters):
    WARNING: Never kill your grandfather. Warranty void if you were never born.

DECISION RECORD — candidates weighed:

1. CHOSEN — "WARNING: Do not kill your grandfather. Warranty void if you
   were never born." (76 chars)
   The grandfather paradox is the real hazard, but the joke never says
   "paradox". The first sentence is a plain safety instruction; the second
   is a warranty clause, the driest official language there is, and it
   quietly assumes the reader has already erased himself. The surprise —
   "if you were never born" — is the last four words. Nothing is wasted:
   "WARNING:" sets the label frame, "Warranty void" carries the whole
   straight-faced joke, and "never born" is the punch.

2. "WARNING: If you meet yourself, do not lend him money. He will not pay
   you back." (80 chars)
   The duplicate-self hazard is real and the last line lands, but the money
   gag is a generic debtor joke that would work for a twin, a clone, or a
   roommate. The hazard is only the setup; the joke is not the hazard.

3. "WARNING: Do not wave at yourself. He already knows what you did."
   (64 chars)
   Creepy and short, and the duplicate self is there, but "what you did"
   is vague — the reader has to invent the joke, and the label never tells
   them what the hazard actually is. It hints at a paradox instead of
   turning one into the joke.

4. "WARNING: Passengers arriving before they depart will be charged
   twice." (75 chars)
   The bureaucratic tone is exactly right and it is funny, but the hazard
   is a fare, not a real danger of time travel. It names a scheduling
   quirk flatly rather than turning a paradox into the joke, so it loses
   on criterion 2 to the chosen line.

WRITING PASSES (2 genuine passes on the chosen line):

Pass 1: "WARNING: Do not kill your grandfather, or you will never be
born."
   Flat. It states the paradox as a consequence, so there is no surprise:
   the reader knows where it is going by the comma. "Or you will never be
   born" is a warning, not a punch, and the label reads like a textbook
   explaining the paradox instead of a product warning.

Pass 2 (final): "WARNING: Do not kill your grandfather. Warranty void if
you were never born."
   Split into two sentences so the first reads as a real instruction and
   the second as fine print. Reframed the consequence as a warranty
   clause: the manufacturer is not worried about you, it is worried about
   its liability, and "if you were never born" arrives as the last four
   words — the reader discovers the paradox only after the label has
   already voided them. "Cannot" was never in play; the dry "void" does
   the work of the whole joke.

Why it wins: it is the only candidate where the hazard IS the joke (the
paradox, delivered as a warranty exclusion), the surprise is saved for the
end, and the voice never breaks character — it reads like something
printed on the box.

REVISION PASS (24 Nov 2026):

Honest critique of the submitted line. Strengths that survived every
challenge: the warranty clause is the driest official language there is,
and it turns the paradox itself into the joke instead of explaining it;
"if you were never born" lands the surprise in the last four words; the
second-person "you" is the emotional hook — the label addresses a reader
who does not exist. Real weaknesses found: (a) the setup, "Do not kill
your grandfather", spends two words ("Do not") on a prohibition a label
states in one; (b) the grandfather paradox is the most famous time-travel
joke in the world, so the line lives or dies on the warranty frame, not
the setup — the frame has to carry the whole laugh.

Fresh alternatives weighed and cut:

A. "WARNING: Do not kill your grandfather. He is the only spare part we
   cannot replace." (79 chars)
   Genuinely funny — the grandfather as an irreplaceable part — but the
   joke is about the parts inventory, and the paradox (your own
   non-existence) is only implied, never the joke itself. Loses on
   criterion 2 to the warranty version, where the paradox IS the joke.

B. "WARNING: Do not kill your grandfather. Your birth certificate is
   also void." (74 chars)
   The "also" does clever work (it implies the warranty is already void)
   and a voided birth certificate is a fresher object than a warranty.
   But it drops the word "warranty" entirely, and the warranty clause is
   the label frame — without it the line is a quip, not a product notice.
   Loses on criterion 4; kept in mind, not used.

C. "WARNING: Do not kill your grandfather. This voids your warranty and
   your birth certificate." (84 chars)
   Two bureaucratic objects, punch on "birth certificate" — but it is two
   jokes in one sentence, the second one better than the first, which
   means the first is dead weight. Loses on criterion 5. The shorter
   birth-certificate variant (B) was the salvage of this idea, and it
   lost for the reason above.

D. "Warranty void if never born." (tightening the second sentence, 67
   chars total)
   Snappier, and the missing "you were" even mirrors the reader's
   non-existence — but dropping the second person drops the hook. The
   label has to talk to somebody to void them. Rejected; "if you were
   never born" stays.

E. "Warranty void if you never existed." (76 chars total)
   Colder and more absolute than "were never born", but "born" is the
   concrete event and the more vivid image; "existed" is philosophy, not
   a label. Rejected.

The one change made — before/after:

BEFORE: "WARNING: Do not kill your grandfather. Warranty void if you were
never born." (76 chars)
AFTER:  "WARNING: Never kill your grandfather. Warranty void if you were
never born." (75 chars)

"Do not" became "Never": one word does the work of two, the rhythm
snaps harder ("Never kill" is a real warning-label cadence — "Never
operate…", "Never mix…"), and nothing is lost, since "Never" is the
same absolute prohibition. The rest of the line survived every challenge
above, so it stands unchanged: the warranty frame, the "you", and the
last-four-words punch are all doing work no alternative did better.
"""

import os
import sys

LINE = "WARNING: Never kill your grandfather. Warranty void if you were never born."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    path = os.path.join(out_dir, "entry.txt")
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)
    # Read-back verification: the file must hold exactly the intended line.
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    entry = content.rstrip("\n")
    assert entry == LINE, f"entry.txt mismatch: {entry!r} != {LINE!r}"
    assert 1 <= len(entry) <= 120, f"gate failed: {len(entry)} chars, need 1-120"
    print(f"Verified: {len(entry)} characters, 1 line.")


if __name__ == "__main__":
    main()
