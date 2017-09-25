def decrypt(encrypted_text, n):
    if encrypted_text == "":
        return ""
    elif encrypted_text is None:
        return None
    elif n <= 0:
        return encrypted_text
    raw = list(encrypted_text)
    length = len(encrypted_text)
    qianLen = length // 2
    for i in range(n):
        count = 0
        qianArr = raw[0:qianLen]
        houArr = raw[qianLen:]
        for j in houArr:
            qianArr.insert(count, j)
            count += 2
        raw = qianArr
    return ''.join(qianArr)


def encrypt(text, n):
    if text == "":
        return ""
    elif text is None:
        return None
    elif n <= 0:
        return text
    arr = list(text)
    for i in range(n):
        j = arr[1::2]
        k = arr[0::2]
        j.extend(k)
        arr = j
    result = ''.join(j)
    return ''.join(result)
