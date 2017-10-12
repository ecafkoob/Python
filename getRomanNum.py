import re
def getRomanNum(RomanStr):
    """罗马数字转换成阿拉伯数字,RomanStr是出入的罗马字符串"""
    if re.search('^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$', RomanStr) is not None:
        NumDic = {"pattern": "", "retNum": 0}
        RomanPattern = {
            "0": ('', '', '', 'M'),
            "1": ('CM', 'CD', 'D', 'C', 100),
            "2": ('XC', 'XL', 'L', 'X', 10),
            "3": ('IX', 'IV', 'V', 'I', 1)
        }
        i = 3
        NumItems = sorted(RomanPattern.items())
        for RomanItem in NumItems:
            if RomanItem[0] != '0':
                patstr = NumDic["pattern"].join(['', RomanItem[1][0]])
                if re.search(patstr, RomanStr) is not None:
                    NumDic["retNum"] += 9 * RomanItem[1][4]
                    NumDic["pattern"] = patstr
                else:
                    patstr = NumDic["pattern"].join(['', RomanItem[1][1]])
                    if re.search(patstr, RomanStr) is not None:
                        NumDic["retNum"] += 4 * RomanItem[1][4]
                        NumDic["pattern"] = patstr
                    else:
                        patstr = NumDic["pattern"].join(['', RomanItem[1][2]])
                        if re.search(patstr, RomanStr) is not None:
                            NumDic["retNum"] += 5 * RomanItem[1][4]
                            NumDic["pattern"] = patstr
            if NumDic["pattern"] == '':
                NumDic["pattern"] = '^'
            tempstr = ''
            sum = 0
            for k in range(0, 4):
                pstr = RomanItem[1][3].join(['', '{']).join(['', str(k)]).join(['', '}'])
                patstr = NumDic["pattern"].join(['', pstr])
                if re.search(patstr, RomanStr) is not None:
                    sum = k * (10 ** i)
                    tempstr = patstr
            if tempstr != '':
                NumDic["pattern"] = tempstr
            else:
                NumDic["pattern"] = patstr
            NumDic['retNum'] += sum
            i -= 1
        return NumDic['retNum']
    else:
        return 'String is not a valid Roman numerals'