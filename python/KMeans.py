def KMeans(k: int, datas: list):
    centerPoint = [set() for _ in range(k)]
    memberClass = [0 for _ in range(len(datas))]

    while True:
        hasChange = False
        for i in range(len(datas)):
            x, y = datas[i]
            if i < k and not centerPoint[i]:
                centerPoint[i].add(datas[i])
                memberClass[i] = i
            else:
                distance = (float("inf"), -1)
                for j in range(k):
                    caseX = sum([x for x, _ in centerPoint[j]]) / len(centerPoint[j])
                    caseY = sum([y for _, y in centerPoint[j]]) / len(centerPoint[j])
                    curDistance = ((x - caseX) ** 2 + (y - caseY) ** 2, j)
                    distance = min(distance, curDistance)

                if distance[1] != memberClass[i]:
                    hasChange = True

                    if datas[i] in centerPoint[memberClass[i]]:
                        centerPoint[memberClass[i]].remove(datas[i])
                    centerPoint[distance[1]].add(datas[i])
                    memberClass[i] = distance[1]

        if not hasChange:
            break

    print(datas)
    return memberClass


def KMeans_input(k: int):
    # 輸入格式： x1,y1 x2,y2 x3,y3 ...
    datas = input().split()
    datas = [tuple(map(int, v.split(","))) for v in datas]
    return KMeans(k, datas)
