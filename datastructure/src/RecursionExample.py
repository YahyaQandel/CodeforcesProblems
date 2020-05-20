class RecursionExample:

    def strip_zeros(self, text):
        if text[0] == "0":
            text = self.strip_zeros(text[1:])
        return text
