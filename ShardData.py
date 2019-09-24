import pandas
from random import shuffle


class ShardData(object):

    def __init__(self):
        print(self.__hash__)

    def shard_train_test(self, source, auth_data=False):
        if not auth_data:
            train_proportion = 0.8
        else:
            train_proportion = 0.95

        baseName = source.rsplit('.', 1)[0]
        train_file = f'{baseName}_train.txt'
        test_file = f'{baseName}_test.txt'

        handel = pandas.read_csv(source, index_col=False, low_memory=False)

        train_data_set = []
        test_data_set = []

        for head in list(handel.head()):
            train_num = int(handel[head].dropna().__len__() * train_proportion)
            sub_list = [
                f'__label__{head},{item.strip()}\n'for item in handel[head].dropna().tolist()]

            train_data_set.extend(sub_list[:train_num])
            test_data_set.extend(sub_list[train_num:])

        shuffle(train_data_set)
        shuffle(test_data_set)

        with open(train_file, 'w', encoding='utf-8') as trainf,\
                open(test_file, 'w', encoding='utf-8') as testf:
            for tds in train_data_set:
                trainf.write(tds)
            for tsds in test_data_set:
                testf.write(tsds)

        return train_file, test_file


if __name__ == "__main__":
    import TransformData as td
    td = td.TransformData()
    handler = open(r'C:\Store\data.txt', encoding='utf-8')
    td.to_csv(handler, 'data.txt')
    handler.close()

    sd = ShardData()
    train_file, test_file = sd.shard_train_test('data.csv', auth_data=True)
