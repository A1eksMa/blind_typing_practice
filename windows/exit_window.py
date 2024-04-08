def exit_window(max_height, max_width):

    import curses
    from curses.textpad import Textbox, rectangle

    from windows.main_window import main_window

    curses.curs_set(False)

    left_and_right_padding = 12
    exit_win_width = max_width - 2*left_and_right_padding

    top_padding = 10
    exit_win_height = max_height - 2*top_padding

    min_exit_win_height = 10
    if exit_win_height < min_exit_win_height:
        exit_win_height = min_exit_win_heigh

    buttons_row = exit_win_height - 5

    exit_win = curses.newwin( exit_win_height,
                              exit_win_width,
                              top_padding,
                              left_and_right_padding)

    exit_win.bkgd(' ', curses.color_pair(5))
    exit_win.keypad(True)

    title = 'Statistics:'
    exit_win.addstr(3, 0, title.center(exit_win_width))
    exit_win.addstr('\n\n')
    message = 'Press any key to continue or Esc to exit'
    exit_win.addstr(message.center(exit_win_width))

    exit_win.noutrefresh()

    # Draw rectangle frame
    rectangle_height = exit_win_height - 2
    rectangle_width = exit_win_width - 2
    rectangle(exit_win, 1, 1, rectangle_height, rectangle_width)
    
    exit_win.noutrefresh()
    curses.doupdate()

    # Add two buttons
    button1 = "  Continue  "
    button2 = "    Exit    "
    active_button = 1

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
        exit_win.refresh()
    
    draw_buttons(active_button)
    
   
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
        else:
            if active_button == 1:
                active_button = 2
            elif active_button == 2:
                active_button = 1
                
            
            #if user_input == ord('d'):
                #active_button = 2 if active_button == 1 else 1
            #elif user_input == ord('a'):
                #active_button = 1 if active_button == 2 else 2
        
            draw_buttons(active_button)
            exit_win.addstr(0, 0, f"Button {active_button} selected", curses.color_pair(2))
            exit_win.refresh()
