def start_window(max_height, max_width, debug_mode = False):

    import curses
    from curses.textpad import rectangle
    from windows.main_window import main_window

    path_to_file = ''

    # Curses settings
    curses.curs_set(True)

    # Set width start window
    left_and_right_padding = 12
    start_win_width = max_width - 2*left_and_right_padding

    # Set height start window
    top_padding = 10
    start_win_height = max_height - 2*top_padding

    min_start_win_height = 10
    if start_win_height < min_start_win_height:
        start_win_height = min_start_win_heigh

    # Init start window
    start_win = curses.newwin(start_win_height,
                              start_win_width,
                              top_padding,
                              left_and_right_padding)

    start_win.bkgd(' ', curses.color_pair(5))
    start_win.keypad(True)

    # Content of exit window
    title = 'Welcome to Blind Typing Practice!'
    start_win.addstr(3, 0, title.center(start_win_width))
    message = 'Input path to typing file and press Enter to continue (or Esc to exit)'
    start_win.addstr(5, 0 ,message.center(start_win_width))

   start_win.noutrefresh()

    # Draw rectangle frame
    rectangle_height = start_win_height - 2
    rectangle_width = start_win_width - 2
    rectangle(start_win, 1, 1, rectangle_height, rectangle_width)
    
    start_win.noutrefresh()

    # Draw input form
    def draw_input_box():
        input_box_padding = 3
        lenght = start_win_width - 2*input_box_padding
        
        message = "Path to file: "
        
        start_win.addstr(9, input_box_padding, message)
        start_win.addstr(9, input_box_padding + len(message), path_to_file, curses.color_pair(1))
        spaces = lenght - input_box_padding + len(message) + len(path_to_file)
        start_win.addstr(9, input_box_padding + len(message) + len(path_to_file), ''*spaces, curses.color_pair(1))
    
    draw_input_box()

    start_win.noutrefresh()

    curses.doupdate()
    
    while True:
        user_input = start_win.getch()
        if user_input == 27:
            break
        elif user_input in [10,13,curses.KEY_ENTER]:
            main_window(max_height, max_width)
        elif user_input == curses.KEY_BACKSPACE:
            path_to_file = path_to_file[:-1]
            start_win.addstr(9, 3, f"Path to file: {path_to_file} ", curses.color_pair(1))
            start_win.refresh()
        else:
            path_to_file += chr(user_input)
            start_win.addstr(9, 3, f"Path to file: {path_to_file} ", curses.color_pair(1))
            start_win.refresh()
            
        if debug_mode:
            start_win.addstr(0, 0, f"Press {chr(user_input)}", curses.color_pair(2))
            start_win.refresh()
