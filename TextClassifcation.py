import os
import numpy as np
import fasttext.FastText as fasttext

# model = fasttext.train_supervised(input=r'C:\Store\data.txt')
# model.save_model(r'Chinese_Model.bin')
# model.predict("死侍真的太贱了")


def train(ipt=None, opt=None, model='.', dim: int = 100, epoch: int = 5, lr: float = 0.1, loss='softmax'):
    np.set_printoptions(suppress=True)

    if os.path.isfile(model):
        classifier = fasttext.load_model(model)
    else:
        classifier = fasttext.train_supervised(
            ipt, label='__label__', dim=dim, epoch=epoch, lr=lr, wordNgrams=2, loss=loss)
        classifier.save_model(opt)
    return classifier


class TextClassifcation(object):

    def train_model(self, ipt=None, opt=None, model='.', dim: int = 100, epoch: int = 5, lr: float = 0.1, loss='softmax'):
        return train(ipt=ipt, opt=opt, model=model, dim=dim, epoch=epoch, lr=lr, loss=loss)


if __name__ == "__main__":
    dim = 100
    lr = 0.5
    epoch = 5
    model = f'FastTx_dim{dim}-{lr}-{epoch}.model'

    tcf = TextClassifcation()
    classifier = tcf.train_model(ipt=r'C:\PyWorkspaces\SourceCore\pynlu\Datas\data.txt', opt=model, model=model,
                                 dim=dim, epoch=epoch, lr=lr)
    result = classifier.test(
        r'C:\PyWorkspaces\SourceCore\pynlu\Datas\data.txt')
    prdic= classifier.predict('2019年10月1日是中华人民共和国成立70周年纪念日。庆祝中华人民共和国成立70周年大会10月1日举行，习近平将发表重要讲话。庆祝大会后，将举行盛大的庆祝中华人民共和国成立70周年阅兵式和群众游行。', k=-1)
    print(result,prdic)
