with open("input", "r") as f:
    data = f.read()

sp = (x.split() for x in data.splitlines())
left, right = (sorted(t) for t in zip(*sp))

print(sum(int(max(l, r)) - int(min(l, r)) for l, r in zip(left, right)))
print(sum(int(l) * right.count(l) for l in left))
