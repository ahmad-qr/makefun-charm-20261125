"""A one-line weather forecast for a city that does not exist.

Writes the forecast to /output/entry.txt for make.fun's
"Charm the Commuter: Forecast a City That Isn't" bounty.
Stdlib only, deterministic, no network, no randomness.
"""

import os

LINE = (
    "Tomorrow in Nowhereton: light rain, heavy sighs, and a 100% "
    "chance the bus is late again. Bring an umbrella and a grudge."
)


def main():
    # The sealed gate: /output/entry.txt must be UTF-8 text of
    # 1 to 140 characters, not only white space.
    text = LINE.strip()
    assert 1 <= len(text) <= 140, "line must be 1-140 characters"
    assert text.strip(), "line must not be only white space"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
