import re
import jieba

from types import FunctionType, MethodType


def clean_text(raw: str):
    fil = re.compile(r"[^0-9a-zA-Z\u4e00-\u9fa5]+")  # 匹配一个中文或多个中文
    return fil.sub(' ', raw)


def seg(sentence: str, sw, apply: type = None):
    if(isinstance(apply, FunctionType) or isinstance(apply, MethodType)):
        sentence = apply(sentence)
    return ' '.join([i for i in jieba.cut(sentence) if i.strip() and i not in sw])


def stop_words(path: str):  # 加载停用词
    with open(path, 'r', encoding='utf-8') as swf:
        return [line.strip() for line in swf]


class Filtering():

    def __init__(self, path: str):
        self.path = path

    def parse(self, content: str):
        res: str = seg(content.lower().replace('\n', ''),
                       stop_words(self.path), apply=clean_text)
        return res


if __name__ == "__main__":
    f = Filtering(path=r'C:\PyWorkspaces\SourceCore\pynlu\Datas\stopwords.txt')
    result = f.parse(
        '70年峥嵘岁月，70年光辉历程，70年砥砺前行，新中国的发展和崛起承载着历史的风霜，沉淀着中国人民不可复制的记忆。')
    print(result)
