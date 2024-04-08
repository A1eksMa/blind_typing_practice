from windows import *


# System settings
class Settings():
    def __init__(self):
        # Path to file
        self.path_to_file = ''
    
    def get_display(self):
        height = curses.LINES - 1
        width = curses.COLS - 1
        return height, width
       
        

             
user_settings = Settings()

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
    
    main_window(user_settings, True)


# Start script
curses.wrapper(main)
