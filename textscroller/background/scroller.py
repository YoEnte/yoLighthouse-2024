from textscroller.background.text import *

class Scroller:
    def __init__(self, text: Text, tps: int = 1, color: tuple[int] = (255, 255, 255), back_color: tuple[int] = (0, 0, 0)):
        
        self.text = text
        self.color = color
        self.background_color = back_color
        self.tps = tps
        self.frame_count = 0
        self.current_bool_frame = []
        self.current_frame = []
        self.next_frame(True)

    def next_frame(self, first: bool = False):
        
        self.current_bool_frame = []
        self.current_frame = []

        for row in range(14):

            new_bool_frame_row = []

            new_bool_frame_row += self.text.rendered_text[row][self.frame_count:self.frame_count + 28]

            if len(new_bool_frame_row) < 28:
                new_bool_frame_row += self.text.rendered_text[row][:28 - len(new_bool_frame_row)]

            new_frame_row = []
            for n in new_bool_frame_row:
                if n == 0:
                    new_frame_row.append(self.background_color)
                else:
                    new_frame_row.append(self.color)

            self.current_bool_frame.append(new_bool_frame_row)
            self.current_frame.append(new_frame_row)
            
        if not first:
            Text.pretty_print(self.text.text, self.current_bool_frame)
            print(len(self.current_bool_frame[0]))

            self.frame_count += 1
            self.frame_count = self.frame_count % len(self.text.rendered_text[0]) # reset to 0 at end of render