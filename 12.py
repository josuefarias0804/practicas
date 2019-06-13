a = {'a': 1}
b = {'b': 2}

d = dict(a, **b)
d.update({'c': 3})
print(d)

print({
    **a,
    **b,
    'c':3,
})