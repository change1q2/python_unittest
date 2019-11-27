from configparser import ConfigParser


class MyConf(ConfigParser):

    def __init__(self, filename, encoding):
        super().__init__()
        self.filename = filename
        self.encoding = encoding
#读取数据
    def read_(self):
        return super().read(filenames=self.filename, encoding=self.encoding)

    def get(self, section, option):
        return super().get(section, option)

    def write(self, section, option, value):
        super().set(section, option, value)

"""
这个类封装没讲完，可以先不写 下节课讲完再写


"""