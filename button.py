from utils.draw_utils import draw_algo_button


class Button:
    def __init__(self, screen, start_x, end_x, start_y, end_y, button_name):
        self.start_x = start_x
        self.end_x = end_x
        self.start_y = start_y
        self.end_y = end_y
        self.button_name = button_name
        # draw the button
        draw_algo_button(screen, start_x, end_x, start_y, end_y, button_name)

    def is_pressed(self, mouse):
        if self.start_y <= mouse[1] <= self.start_y + self.end_y and \
                self.start_x <= mouse[0] <= self.start_x + self.end_x:
            return True
        return False
