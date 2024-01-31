
a = set()
for i in range(10):
    for j in range(10):
        for s in range(10):
            for k in range(10):
                if len({i, j, s, k}) == 4:
                    a.add(f'{i}{j}{s}{k}')


v = '1234'
while True:
    s = sorted(list(a), key=lambda e: sum([abs(int(e[i]) - int(v[i])) for i in range(4)]))
    if not s:
        print('Такого случая не может быть!')
        break
    elif len(s) == 1:
        print(f'Вы загадали число {s[0]}!')
        break
    bc = input(f'Осталось {len(a)} вариантов, попробуйте {s[-1]}. \nПосле введите кол-во быков и коров: ')
    bc = (int(bc[0]), int(bc[1]))
    v = s[-1]

    to_del = set()
    for r in a:
        bulls = sum([1 for i in range(4) if v[i] == r[i]])
        cows = sum([1 for i in range(4) if v[i] != r[i] and v[i] in r])

        if (bulls, cows) != bc:
            to_del.add(r)
    a -= to_del
