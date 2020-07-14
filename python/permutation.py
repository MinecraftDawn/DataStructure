def perm(datas: list, index: int) -> None:
    if index == len(datas):
        print(datas)
    else:
        for i in range(index, len(datas)):
            datas[index], datas[i] = datas[i], datas[index]
            perm(datas, index + 1)
            datas[index], datas[i] = datas[i], datas[index]


def permYield(datas: list):
    if len(datas) <= 1:
        yield datas
    else:
        for p in permYield(datas[1:]):
            for i in range(len(datas)):
                yield p[:i] + [datas[0]] + p[i:]
