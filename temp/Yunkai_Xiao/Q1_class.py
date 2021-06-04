class StatWord:
    def __init__(self, filename=None, verbose=True):
        self.text = ""
        self.word_counter = {}
        self.__char_check = r"abcdefghijklmnopqrstuvwxyz" \
                "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789" \
                " ~!@#$%^&*()_+=-`[]\{}|:\";',./<>?，。、　" \
                "《》？；’：”“【】、｛｝§=-+——）（*&……%￥#@！～·\n"
        if filename is not None and len(filename) > 0:
            self.read_text(filename)
            self.stat_char()
            if verbose:
                self.print_res()
    
    def read_text(self, filename: str):
        with open(filename, 'rt', encoding="utf-8", errors="ignore") as f:
            self.text = f.read()

    def stat_char(self):
        if len(self.text) == 0: return
        text = self.text
        for c in self.__char_check:
            text = text.replace(c, "")
        for c in text:
            if c not in self.word_counter:
                self.word_counter[c] = text.count(c)
        self.word_counter = dict(sorted(self.word_counter.items(), key=lambda x: x[1], reverse=True))

    def print_res(self):
        print("总字数：", len(self.text))
        print("用字数：", len(self.word_counter))
        print("最常用百字频率如下：")
        for i, c in zip(range(100), self.word_counter):
            print("{}：{:>5d}".format(c, self.word_counter[c]))

if __name__ == '__main__':
    filename = "c:/Users/1/Desktop/cxj.txt"
    res = StatWord(filename)
