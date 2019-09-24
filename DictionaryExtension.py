
class dictionaryExtension(object):

    data_Mapper: dict = {
        str: '',
        int: 0,
        list: list,
        dict: dict,
        set: set,
        bool: False,
        float: .0
    }

    def __init__(self, obj, default=None):
        self.dict = {}
        assert obj in self.data_Mapper, \
            '类型错误'
        self.t = obj
        if default is None:
            return
        assert isinstance(default, obj), \
            f"默认（{default}）是 {obj}"
        self.v = default

    def __setitem__(self, key, value):
        self.dict[key] = value

    def __getitem__(self, item):
        if item not in self.dict and hasattr(self, 'v'):
            self.dict[item] = self.v
            return self.v
        elif item not in self.dict:
            if callable(self.data_Mapper[self.t]):
                self.dict[item] = self.data_Mapper[self.t]()
            else:
                self.dict[item] = self.data_Mapper[self.t]
            return self.dict[item]
        return self.dict[item]
