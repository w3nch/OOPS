func = []

for i in range(4):
    func.append(lambda: i)

for f in func:
    print(f())
