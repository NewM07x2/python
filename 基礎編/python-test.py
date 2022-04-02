from logging import exception

from pyrsistent import thaw


print('hello')

A = [1, 2, 3, 4, ]
B = A
B = [100, 2, 3, 4, ]

print(A)
print(B)

num = 1

print(num)
print(num, type(num))
print("hello \nこんにちわ！")
print(r"C:\name\name")
print("#############")
print("""\
line1
line2
line3\
""")
print("#############")


a = 'a'
print(f'a is {a}')

x, y, z = 1, 2, 3
print(f'a is {x}, {y}, {z}')
print(f'a is {z}, {y}, {x}')

name = 'Jun'
family = 'Sakai'
print(f'My name is {name} {family}. Watashi ha {family} {name}')

s = ['a', 'b']
q = ['x', 'y', 'z']
a = [s, q]
print(a[0][0])

g = ['x', 'y', 'z']
g[0] = 'test'
print(g)

n = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(n)
n.append(100)
print(n)
n.insert(0, 1000)
print(n)
n.pop()
print(n)
n.pop(2)
print(n)

del n[0]
print(n)

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]
a += b
print(f'a is {a}')
# 変数としてaを定義して代入する形

r = [1, 2, 3, 4, 5]
print(r.index(3))  # '3'がリスト内の半番目のindexに入っているかを表示する
print(r.count(3))  # '3'がリスト内にいくつ入っているかを表示する。

s = 'My name is Masato'
to_split = s.split(' ')  # 半角で区切りリストへ挿入する
print(to_split)
x = ' '.join(to_split)  # 半角でリスト内を連結させる
print(x)

# タプル：書き換え不可のリスト

s = 'aaaaaa' \
    + 'bbbb'
print(s)

a = 100
if a == 10:
    print('10です')
elif a != 10:
    print('10ではない')
else:
    print('10ではない2')

# print('-----------------')
# a = ['*', '*', '*', '*', '*']
# count = 2
# while count < 3:
#     print(a[count])
#     print(a[count-1] + a[count] + a[count+1])
#     count += 1
# heigth = 10
# while heigth != 0:
#     print('*' * heigth)
#     heigth -= 1


n.insert(0, 1000)
print(n)
n.insert(len(n), 999)
print(n)

for _ in range(10):  # 10ループする
    print('*')

for i, value in enumerate(['1', '2', '3']):
    print(i, value)

days = [
    'Mon',
    'Tue',
    'Wed'
]
eats = [
    'apple',
    'orange',
    'banana'
]
# zip関数：複数関数のindexをまとめた行う
for day, eat in zip(days, eats):
    print(day, eat)

# def say():
#     s = 'hey!'
#     return s
# s = say()
# print(s)

word = input()


def sayword(word):
    return 'あなたは' + word + 'と言いました。'


result = sayword(word)
print(result)

print('test')


