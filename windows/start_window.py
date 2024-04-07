def start_window(max_height, max_width):

    import curses
    from curses.textpad import Textbox, rectangle

    from windows.main_window import main_window

    left_and_right_padding = 12
    start_win_width = max_width - 2*left_and_right_padding

    top_padding = 10
    start_win_height = max_height - 2*top_padding

    min_start_win_height = 10
    if start_win_height < min_start_win_height:
        start_win_height = min_start_win_height

    start_win = curses.newwin(start_win_height,
                              start_win_width,
                              top_padding,
                              left_and_right_padding)

    start_win.bkgd(' ', curses.color_pair(2))

    title = 'Welcome to Blind Typing Practice!'
    start_win.addstr(3,
                     0,
                     title.center(start_win_width),
                     curses.color_pair(2))
    start_win.addstr('\n\n')
    message = 'Press any key to continue or Esc to exit'
    start_win.addstr(message.center(start_win_width))

    start_win.noutrefresh()

    # Draw rectangle frame
    rectangle_height = start_win_height - 2
    rectangle_width = start_win_width - 2
    rectangle(start_win, 1, 1, rectangle_height, rectangle_width)

    curses.curs_set(False)
    start_win.noutrefresh()
    curses.doupdate()

    while True:
        user_input = start_win.getch()
        if user_input == 27:
            break
        else:
            start_win.clear()
            start_win.refresh()
            main_window(max_height, max_width)
