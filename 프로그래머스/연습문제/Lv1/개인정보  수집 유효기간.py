def solution(today, terms, privacies):
    # today 계산
    ty, tm, td = map(int, today.split('.'))
    todayDay = (ty - 2000) * 28 * 12 + (tm - 1) * (28) + td

    # terms 처리
    termDict = dict()
    for term in terms:
        alpha, month = term.split()
        termDict[alpha] = int(month) * 28  # int(month*28) 하면 오류난다. 문자열을 28번 반복하겠다는 뜻이니까

    # privacies 분류(메인)
    res = []
    for i, p in enumerate(privacies):
        date, alpha = p.split()
        py, pm, pd = map(int, date.split('.'))
        privacyDay = (py - 2000) * 28 * 12 + (pm - 1) * (28) + pd
        if todayDay >= privacyDay + termDict[alpha]:
            res.append(i + 1)

    return res