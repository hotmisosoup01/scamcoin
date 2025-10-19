import sys
import time
import itertools
import os
import random

# --- Configurable settings ---
MESSAGE = "Hello Wrld"
TYPE_DELAY = 0.08          # seconds between each character
LINE_DELAY = 0.4           # delay after finishing one line
SPINNER_SPEED = 0.05       # speed of spinner animation
COLORS = [
    "\033[91m", "\033[92m", "\033[93m",
    "\033[94m", "\033[95m", "\033[96m"
]
RESET = "\033[0m"
# ------------------------------

class Spinner:
    def __init__(self, symbols="|/-\\"):
        self.cycle = itertools.cycle(symbols)

    def spin_once(self):
        sys.stdout.write(next(self.cycle))
        sys.stdout.flush()
        time.sleep(SPINNER_SPEED)
        sys.stdout.write("\b")

def type_out(text, color):
    """Print text as if being typed."""
    for char in text:
        sys.stdout.write(color + char + RESET)
        sys.stdout.flush()
        time.sleep(TYPE_DELAY)
    sys.stdout.write("\n")
    sys.stdout.flush()

def clear():
    os.system("cls" if os.name == "nt" else "clear")

# --- Main loop ---
clear()
spinner = Spinner()
counter = 1
color_cycle = itertools.cycle(COLORS)

print("\033[96mInitializing ScamCoin Print Agent...\033[0m\n")
time.sleep(1)

while True:
    spinner.spin_once()
    color = next(color_cycle)
    prefix = f"[{counter:04d}] "
    type_out(prefix + MESSAGE, color)
    counter += 1
    time.sleep(LINE_DELAY)
