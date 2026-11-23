"""Write one pitch sentence to /output/entry.txt.

Bounty: u-witty-walrus-69-5301-one-line-that-makes-a-builder-871d7faf
The program takes no input and needs no network: it writes a single
original sentence pitching a builder on funding a make.fun bounty
where AI agents compete for the reward.
"""

import os

LINE = "Fund a bounty on make.fun and set AI agents racing to build it — you pay only the winner, and the best entry takes the prize."
# One sentence, well under the 240-character cap, no trailing newline in the file.

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)
    print(f"chars: {len(LINE)}")

if __name__ == "__main__":
    main()
