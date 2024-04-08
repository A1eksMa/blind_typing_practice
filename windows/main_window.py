def main_window(curses, user_settings, debug_mode = False):

    # Curses settings
    curses.curs_set(True)
    max_height, max_width = user_settings.get_display()

    # Init main window
    main_win = curses.newwin(max_height,
                              max_width,
                              0,
                              0)

    main_win.bkgd(' ', curses.color_pair(1))

    # Draw rectangle frame
    rectangle_height = max_height - 2
    rectangle_width = max_width - 2
    curses.textpad.rectangle(main_win, 1, 1, rectangle_height, rectangle_width)

    title = 'Blind Typing Trainer'
    main_win.addstr(0,
                     0,
                     title.center(max_width),
                     curses.color_pair(2))
    


    if debug_mode:
        main_win.addstr(0, 0, f"Path to file: {user_settings.path_to_file}", curses.color_pair(2))
        main_win.refresh()
    
    main_win.refresh()

    with open(user_settings.path_to_file, 'r') as file:
        i=0
        for line in file:
            main_win.addstr(5+i, 5, line, curses.color_pair(2))
            i+=1
    
    main_win.getch()
   #main_win.noutrefresh()
   #curses.doupdate()
