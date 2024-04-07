def main_window(max_height, max_width):
    import curses
    from curses.textpad import Textbox, rectangle
    curses.curs_set(True)

    main_window = curses.newwin(max_height,
                              max_width,
                              0,
                              0)

    main_window.bkgd(' ', curses.color_pair(2))

    # Draw rectangle frame
    rectangle_height = max_height - 2
    rectangle_width = max_width - 2
    rectangle(main_window, 1, 1, rectangle_height, rectangle_width)

    title = 'Blind Typing Trainer'
    main_window.addstr(0,
                     0,
                     title.center(max_width),
                     curses.color_pair(2))

    main_window.refresh()
    main_window.getch()
   #main_window.noutrefresh()
   #curses.doupdate()
