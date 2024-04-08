    def draw_rectangle(win, height, width, start_y, start_x):
        for y in range(start_y, start_y + height):
            win.addch(y, start_x, '|')  # Vertical lines
            win.addch(y, start_x + width - 1, '|')
        for x in range(start_x, start_x + width):
            win.addch(start_y, x, '-')  # Horizontal lines
            win.addch(start_y + height - 1, x, '-')
