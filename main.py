import os
import sys
import curses
from curses.textpad import Textbox, rectangle

from windows.start_window import *
from windows.main_window import *
from windows.exit_window import *


# System settings

# Path to file
path_name = ''

# Timing
started_time = None
current_time = None
duration = 0

# Statistics
typed_keys = 0
typed_right = 0

speed = 0
accuracy = 0

# Errors
errors = 0
expected_input = None
user_input = None


def main(stdscr):

    # System preferences
    max_width = curses.COLS - 1
    max_height = curses.LINES - 1

    # System palette
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_RED)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_GREEN)
    curses.init_pair(4, curses.COLOR_BLACK, curses.COLOR_YELLOW)
    curses.init_pair(5, curses.COLOR_BLACK, curses.COLOR_BLUE)
    curses.init_pair(6, curses.COLOR_BLACK, curses.COLOR_MAGENTA)
    curses.init_pair(7, curses.COLOR_BLACK, curses.COLOR_CYAN)
    curses.init_pair(8, curses.COLOR_BLACK, curses.COLOR_WHITE)

    stdscr.clear()
    stdscr.bkgd(' ', curses.color_pair(1))
    stdscr.refresh()

    exit_window(max_height, max_width)


# Start script
curses.wrapper(main)
