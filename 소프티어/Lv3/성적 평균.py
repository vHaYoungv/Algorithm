n, k = map(int, input().split())
slist = list(map(int, input().split()))
sumlist = [0]
ssum = 0
for x in slist:
    ssum += x
    sumlist.append(ssum)
for i in range(k):
    a, b = map(int, input().split())
    if a == 1:
        print("{:.2f}".format(round(sumlist[b] / b, 2)))
    else:
        print("{:.2f}".format(round((sumlist[b] - sumlist[a - 1]) / (b - a + 1), 2)))
