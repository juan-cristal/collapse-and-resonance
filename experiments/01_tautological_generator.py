"""
Tautological Generator

A system that:
- has no memory
- does not observe its own output
- cannot change its behavior
- produces sequences that have no meaning inside the system

Any interpretation exists only outside the generator.
"""

import random

def generator(seed):
    # Fixed ruleset derived entirely from the seed
    random.seed(seed)
    rules = [random.randint(0, 1) for _ in range(8)]

    state = 0
    while True:
        # Transition depends only on rules and current state
        state = rules[state % len(rules)]
        yield state


if __name__ == "__main__":
    g = generator(seed=42)

    for _ in range(32):
        print(next(g))

