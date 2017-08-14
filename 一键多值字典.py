from collections import defaultdict
d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)
d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['b'].add(4)

#defaultdict 字典如果在创建值的时候，没有对应的键则会创建它。