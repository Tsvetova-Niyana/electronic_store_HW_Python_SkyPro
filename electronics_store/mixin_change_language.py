class MixinChangeLanguage:
    def __init__(self, language='EN', **kwargs):
        self.__language = language
        super().__init__(**kwargs)

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        if self.__language == 'EN':
            self.__language = 'RU'
        else:
            self.__language = 'EN'



