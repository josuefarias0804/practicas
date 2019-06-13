a = {'a': 1}
b = {'b': 2}
c = {'c': 3}

d = dict(a, **b); d.update(c)
print(d)