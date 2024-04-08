import curses
from curses.textpad import rectangle
from windows import *
from settings import *
             
user_settings = Settings()

def main(stdscr):

    # Curses settings
    curses.curs_set(True)
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

    start_window(curses, user_settings, True)
    
    stdscr.clear()
    stdscr.refresh()
    
    main_window(curses, user_settings, True)

    stdscr.clear()
    stdscr.refresh()
    
    exit_window(curses, user_settings, True)

# Start script
curses.wrapper(main)
