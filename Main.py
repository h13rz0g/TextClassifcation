
import sys
import ShardData as sdd
import TransformData as tfd
import TextClassifcation as tcf


classifier = None


def main():
    source_file = r"C:\PyWorkspaces\SourceCore\pynlu\Datas\data.txt"
    base_name = source_file.rsplit('.')[0]
    csv_file = base_name+'.csv'

    td = tfd.TransformData()

    with open(source_file, encoding='utf-8') as handler:
        lens = handler.readlines()
        td.to_csv(lens, csv_file)

    sd = sdd.ShardData()
    train_file, test_file = sd.shard_train_test(csv_file, auth_data=True)

    dim = 100
    lr = 0.5
    epoch = 5
    model = f'FastTx_dim{dim}-{lr}-{epoch}.model'

    clf = tcf.TextClassifcation()
    classifier = clf.train_model(ipt=train_file, opt=model, model=model,
                                 dim=dim, epoch=epoch, lr=lr)
    test_result = classifier.test(test_file)
    print(test_result)

    prdic = classifier.predict(
        '2019年10月1日是中华人民共和国成立70周年纪念日。庆祝中华人民共和国成立70周年大会10月1日举行，习近平将发表重要讲话。庆祝大会后，将举行盛大的庆祝中华人民共和国成立70周年阅兵式和群众游行。')
    print(prdic)


if __name__ == "__main__":
    main()
