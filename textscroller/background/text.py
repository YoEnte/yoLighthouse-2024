import json
import os

class Text:
    def __init__(self, text: str = "", font = 'classic'):
        
        self.text = text
        font_file = open(os.path.join(os.path.dirname(__file__), "fonts/classic/font.json"), "r", encoding="utf8")
        raw = font_file.read()
        font_file.close()
        self.font_name = font
        self.font_data = json.loads(raw)
        
        self.rendered_text: list[list[int]] = self.empty_render()

        self.render()
        self.pretty_print(self.text, self.rendered_text)

    def empty_render(self) -> list[list]:
        empty = []
        empty = [[] for _ in range(14)]

        return empty
    
    def render(self):
        self.rendered_text = self.empty_render()
        
        count = 0
        for char in self.text:
            _char = char
            if self.font_data['metadata']['case-sensitive'] == False:
                _char = char.lower()

            if _char not in self.font_data['characters']:
                print(f"Warning: Missing char '{_char}' in font {self.font_name}!")
                continue

            for row in range(14):

                self.rendered_text[row] += self.font_data['characters'][_char][row]

                if char in self.font_data['metadata']['end-sentence-chars']:
                    self.rendered_text[row] += [0 for _ in range(self.font_data['metadata']['sentence-space'])]
                else:
                    self.rendered_text[row] += [0 for _ in range(self.font_data['metadata']['char-space'])]

                if count == len(self.text) - 1:
                    self.rendered_text[row] += [0 for _ in range(self.font_data['metadata']['end-of-text-space'])]

            count += 1

    @staticmethod
    def pretty_print(text: str, rendering: list[list[int]]):
        
        print(f"Total text to be rendered: {text}\n")

        print("---")
        for row in rendering:
            row_string = ''
            for p in row:
                if p == 0:
                    row_string += '  '
                else:
                    row_string += '# '

            print(row_string)
        print("---")