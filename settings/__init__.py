import curses

# User settings
class Preferences():
    def __init__(self):
        # Path to file
        self.path_to_file = ''  

# Timing
class Timing():
    def __init__(self):
        self.started_time = None
        self.finished_time = None
        self.current_time = None
        self.pause_start = None
        self.pause_end = None
        self.pause_total = 0
        
    def pause(self):
        return self.pause_end - self.pause_start
    
    def session_duration_total(self):
        return self.finished_time - self.started_time

    def session_duration(self):
        return self.session_duration_total - self.pause_total 
       


# Statistics
typed_keys = 0
typed_right = 0

speed = 0
accuracy = 0

# Errors
errors = 0
expected_input = None
user_input = None

# Terminal
class Display():
    def __init__(self):
        self.height = None
        self.width = None

    def get_display(self):
        self.height = curses.LINES - 1
        self.width = curses.COLS - 1
        return self.height, self.width

# System settings
class Settings(Preferences, Display, Timing):
    pass







