def exit_window(curses, user_settings, debug_mode = False):
    from windows import main_window

    # Curses settings
    curses.curs_set(True)
    max_height, max_width = user_settings.get_display()

    # Set width exit window
    left_and_right_padding = 12
    exit_win_width = max_width - 2*left_and_right_padding

    # Set height exit window
    top_padding = 10
    exit_win_height = max_height - 2*top_padding

    min_exit_win_height = 10
    if exit_win_height < min_exit_win_height:
        exit_win_height = min_exit_win_heigh

    # Init exit window
    exit_win = curses.newwin( exit_win_height,
                              exit_win_width,
                              top_padding,
                              left_and_right_padding)

    exit_win.bkgd(' ', curses.color_pair(5))
    exit_win.keypad(True)

    # Content of exit window
    title = 'Statistics:'
    exit_win.addstr(3, 0, title.center(exit_win_width))
    
    message = 'Press Tab to move and Enter to confirm'
    exit_win.addstr(exit_win_height-7, 0, message.center(exit_win_width))

    exit_win.noutrefresh()

    # Add two buttons
    button1 = "  Continue  "
    button2 = "    Exit    "
    active_button = 1

    buttons_row = exit_win_height - 5
    button_space = 8*" "
    button_padding = int((exit_win_width - len(button1 + button_space + button2))/2)*" "

    def draw_buttons(active_button):
        if active_button == 1:
            exit_win.addstr(buttons_row, 0, button_padding)
            exit_win.addstr(buttons_row, len(button_padding), button1, curses.color_pair(8))
            exit_win.addstr(buttons_row, len(button_padding+button1), button_space)
            exit_win.addstr(buttons_row, len(button_padding+button1+button_space), button2, curses.color_pair(1))
        elif active_button == 2:
            exit_win.addstr(buttons_row, 0, button_padding)
            exit_win.addstr(buttons_row, len(button_padding), button1, curses.color_pair(1))
            exit_win.addstr(buttons_row, len(button_padding+button1), button_space)
            exit_win.addstr(buttons_row, len(button_padding+button1+button_space), button2, curses.color_pair(8))
        
    draw_buttons(active_button)
    
    exit_win.noutrefresh()
    
    # Draw rectangle frame
    rectangle_height = exit_win_height - 2
    rectangle_width = exit_win_width - 2
    
    curses.textpad.rectangle(exit_win, 1, 1, rectangle_height, rectangle_width)
    
    exit_win.noutrefresh()
    
    curses.doupdate()

    if debug_mode:
        exit_win.addstr(0, 0, f"Button {active_button} selected", curses.color_pair(2))
        exit_win.refresh()
    
    while True:
        
        user_input = exit_win.getch()
        
        if user_input in [10,13,curses.KEY_ENTER]:
            
            if active_button == 1:
                exit_win.clear()
                exit_win.refresh()
                main_window(max_height, max_width)
            elif active_button == 2:
                break
        elif user_input in [9,curses.KEY_BTAB]:
            if active_button == 1: active_button = 2
            elif active_button == 2: active_button = 1
                
            draw_buttons(active_button)
            curses.textpad.rectangle(exit_win, 1, 1, rectangle_height, rectangle_width)
            exit_win.refresh()

            if debug_mode:
                exit_win.addstr(0, 0, f"Button {active_button} selected", curses.color_pair(2))
                exit_win.refresh()
