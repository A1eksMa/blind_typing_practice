# User settings
class Preferences():
    def __init__(self):
        # Path to file
        self.path_to_file = ''  


# System settings
class Settings(Preferences):
    def __init__(self):
        pass

    def get_display(self):
        self.height = curses.LINES - 1
        self.width = curses.COLS - 1
        return self.height, self.width


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
