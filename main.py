count = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
list = []
for c in count:
    value = int(input(f'Digite um valor para: {c}: '))
    list.append(value)
print('-='*30)
print(f'[ {list[0]} ]  [ {list[1]} ]  [ {list[2]} ]')
print(f'[ {list[3]} ]  [ {list[4]} ]  [ {list[5]} ]')
print(f'[ {list[6]} ]  [ {list[7]} ]  [ {list[8]} ]')
