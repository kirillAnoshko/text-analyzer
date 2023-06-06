class Text_analyze:
    def __init__(self, text):
        self.text = text

    def open_file(self):
        content = open(self.text, "r", encoding="UTF-8")
        text = content.read()
        return text
                
            
file1 = Text_analyze("text.txt")
text = file1.open_file()
print(text)
                
