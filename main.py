"""Write one weird job title to /output/entry.txt.

Entry for the make.fun bounty "Weirdest Job Title: Blind Judge
Showdown". Deterministic, standard library only, no network access,
no reading of files outside this repository.
"""

import os

TITLE = "Professional Apologizer for Other People's Parrots"


def main() -> None:
    if not 1 <= len(TITLE) <= 60:
        raise ValueError("title must be 1-60 characters")
    for directory in ("/output", os.path.join(os.getcwd(), "output")):
        try:
            os.makedirs(directory, exist_ok=True)
            path = os.path.join(directory, "entry.txt")
            with open(path, "w", encoding="utf-8", newline="") as handle:
                handle.write(TITLE)
            return
        except OSError:
            continue
    raise OSError("could not write entry.txt to /output or ./output")


if __name__ == "__main__":
    main()
