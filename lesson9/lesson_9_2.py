class TextProcessor:
    def __init__(self):
        self.__punctuation = ('!?,.:;/\-_=+][{}')

    def is_punctuation(self, char):
        return char in self.__punctuation

    def get_clean_string(self, text):
        clean_text = ''
        for char in text:
            if not self.is_punctuation(char):
                clean_text += char
        return clean_text

class TextLoader:

    def __init__(self, text_processor : TextProcessor):
        self.__text_processor = text_processor
        self.__clean_string = ''

    @property
    def clean_string(self):
        print()
        print('Clean string: ')
        return self.__clean_string

    def set_clean_text(self, string):
        self.__clean_string = self.__text_processor.get_clean_string(string)
        return

class DataInterface:

    def __init__(self, text_loader : TextLoader):
        self._text_loader = text_loader

    def process_texts(self, text):
        for row in text:
            self._text_loader.set_clean_text(row)
            print(self._text_loader.clean_string)

txt = input('Text: ')
t_p = TextProcessor()
print(t_p.get_clean_string(txt))

tl = TextLoader(t_p)
tl.set_clean_text(txt)
print(tl.clean_string)

d_i = DataInterface(tl)
list = ['Hi!!!', 'My name??', 'hm....', 'yos...']
d_i.process_texts(list)
