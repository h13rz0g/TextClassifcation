# 正向最大匹配法
class MM(object):
    def __init__(self):
        self.window_size: int = 3

    def cut(self, text: str):
        result: list = []
        index: int = 0
        textLength: int = len(text)
        dic: list(str) = ['研究', '研究生', '生命', '命', '的', '起源']
        while textLength > index:
            for size in range(self.window_size+index, index, -1):
                piece: str = text[index:size]
                if piece in dic:
                    index = size-1
                    break
            index = index+1
            result.append(piece+'-----')
        print(result)


if __name__ == '__main__':
    text = '研究生命的起源'
    tokenizer = MM()
    print(tokenizer.cut(text))
