def start_window(max_height, max_width):

    import curses
    from curses.textpad import Textbox, rectangle

    from windows.main_window import main_window

    curses.curs_set(False)

    left_and_right_padding = 12
    start_win_width = max_width - 2*left_and_right_padding

    top_padding = 10
    start_win_height = max_height - 2*top_padding

    min_start_win_height = 10
    if start_win_height < min_start_win_height:
        start_win_height = min_start_win_heigh

    buttons_row = start_win_height - 5

    start_win = curses.newwin(start_win_height,
                              start_win_width,
                              top_padding,
                              left_and_right_padding)

    start_win.bkgd(' ', curses.color_pair(5))
    start_win.keypad(True)

    title = 'Welcome to Blind Typing Practice!'
    start_win.addstr(3, 0, title.center(start_win_width))
    start_win.addstr('\n\n')
    message = 'Press any key to continue or Esc to exit'
    start_win.addstr(message.center(start_win_width))

    start_win.noutrefresh()

    # Draw rectangle frame
    rectangle_height = start_win_height - 2
    rectangle_width = start_win_width - 2
    rectangle(start_win, 1, 1, rectangle_height, rectangle_width)
    
    start_win.noutrefresh()
    curses.doupdate()

    # Add two buttons
    button1 = "  Continue  "
    button2 = "    Exit    "
    active_button = 1

    button_space = 8*" "
    button_padding = int((start_win_width - len(button1 + button_space + button2))/2)*" "

    def draw_buttons(active_button):
        if active_button == 1:
            start_win.addstr(buttons_row, 0, button_padding)
            start_win.addstr(buttons_row, len(button_padding), button1, curses.color_pair(8))
            start_win.addstr(buttons_row, len(button_padding+button1), button_space)
            start_win.addstr(buttons_row, len(button_padding+button1+button_space), button2, curses.color_pair(1))
        elif active_button == 2:
            start_win.addstr(buttons_row, 0, button_padding)
            start_win.addstr(buttons_row, len(button_padding), button1, curses.color_pair(1))
            start_win.addstr(buttons_row, len(button_padding+button1), button_space)
            start_win.addstr(buttons_row, len(button_padding+button1+button_space), button2, curses.color_pair(8))
        start_win.refresh()
    
    draw_buttons(active_button)
    
    path_to_file = ''

    
    def set_file_path(path_to_file):
        user_input = ''
        while True:
            curses.curs_set(True)
            start_win.clear()
            start_win.addstr(0, 0, user_input)
            start_win.refresh()
            user_input = start_win.getch()
         
            if user_input in [10,13,curses.KEY_ENTER]:
                break
            elif user_input == curses.KEY_BACKSPACE:
                path_to_file = path_to_file[:-1]
            else:
                path_to_file += chr(user_input)
        start_window(max_height, max_width)
    
    set_file_path(path_to_file)

    

    
    start_win.addstr(0, 0, f"Button {active_button} selected, path to file: {path_to_file}", curses.color_pair(2))
    start_win.refresh()
    
    while True:
        user_input = start_win.getch()
        if user_input == 27 or user_input == ord('q'):
            break
        elif user_input == ord('a'):
            active_button = 2 if active_button == 1 else 1
            draw_buttons(active_button)
        elif user_input == ord('d'):
            active_button = 1 if active_button == 2 else 2
            draw_buttons(active_button)
            
        start_win.addstr(0, 0, f"Button {active_button} selected", curses.color_pair(2))
        start_win.refresh()
        
        if user_input in [10,13,curses.KEY_ENTER]:
            if active_button == 1:
                start_win.clear()
                start_win.refresh()
                main_window(max_height, max_width)
            elif active_button == 2:
                break
            

