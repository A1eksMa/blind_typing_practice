import os
import sys
import curses
from curses.textpad import Textbox, rectangle

# System settings

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

    curses.start_color()
    curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLUE)

    stdscr.clear()
    stdscr.bkgd(' ', curses.color_pair(1))
    stdscr.refresh()

    def draw_rectangle(win, height, width, start_y, start_x):
        for y in range(start_y, start_y + height):
            win.addch(y, start_x, '|')  # Vertical lines
            win.addch(y, start_x + width - 1, '|')
        for x in range(start_x, start_x + width):
            win.addch(start_y, x, '-')  # Horizontal lines
            win.addch(start_y + height - 1, x, '-')


    def start_window():

        left_and_right_padding = 12
        start_win_width = max_width - 2*left_and_right_padding

        top_padding = 10
        start_win_height = max_height - 2*top_padding

        min_start_win_height = 10
        if start_win_height < min_start_win_height:
            start_win_height = min_start_win_height

        start_win = curses.newwin(start_win_height,
                                  start_win_width,
                                  top_padding,
                                  left_and_right_padding)

        start_win.bkgd(' ', curses.color_pair(2))

        title = 'Welcome to Blind Typing Practice!'
        start_win.addstr(3,
                         0,
                         title.center(start_win_width),
                         curses.color_pair(2))
        start_win.addstr('\n\n')
        message = 'Press any key to continue or Esc to exit'
        start_win.addstr(message.center(start_win_width))

        start_win.noutrefresh()

        # Draw rectangle frame
        rectangle_height = start_win_height - 2
        rectangle_width = start_win_width - 2
        rectangle(start_win, 1, 1, rectangle_height, rectangle_width)

        curses.curs_set(False)
        start_win.noutrefresh()
        curses.doupdate()

        while True:
            user_input = stdscr.getch()
            if user_input == 27:
                break
            else:
                main_window()

    def main_window():
        stdscr.clear()
        curses.curs_set(True)
        rectangle(main_window, 1, 1, max_height, max_width)
        stdscr.addstr('Blind Typing Trainer'.center(max_width))
        main_window.noutrefresh()
        curses.doupdate()

        for char in 'q':
            while True:
                key = stdscr.getkey()
                if key == char:
                    user_input += key
                    break
                else:
                    stdscr.addstr('    '+key)
                    stdscr.refresh()

    def exit_window():
        pass

    start_window()


# Start script
curses.wrapper(main)
