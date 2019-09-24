import pandas
import DictionaryExtension as de
from random import shuffle


def defaultDict(obj, default=None):
    return de.dictionaryExtension(obj, default)


class TransformData(object):

    def __init__(self):
        print(self.__hash__)

    def to_csv(self, handler, output, index: bool = False):
        dd = defaultDict(list)
        for line in handler:
            label, content = line.split(',', 1)
            dd[label.strip('__label__').strip()].append(content.strip())

        df = pandas.DataFrame()
        for key in dd.dict:
            col = pandas.Series(dd[key], name=key)
            df = pandas.concat([df, col], axis=1)

        return df.to_csv(output, index=index, encoding='utf-8')
