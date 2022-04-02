# -*- coding: utf-8 -*-
'''
    変数宣言
'''
# num = 1
# print(num)
# print(num, type(num))

# str = '1'
# print(str, str, sep=',')

# print('test1', 'test2', sep=',', end='\n')

'''
    数学関数
'''
# import math
# result = math.sqrt(25)
# print(result)


'''
    文字列
'''
# print("I am masato")
# print('I\'m masato')

# name = 'masato'
# print(len(name))
# "##############"
# # 何個存在しているか
# print(name.count("m"))
# # 存在確認
# print(name.find("masar"))

# if name.find("5") > 0:
#     print("存在している")
# else:
#     print("存在していない")

# a = 'a'
# print(f'a is {a}')

# x, y, z = 1, 2, 3
# print(f'a is {x}, {y}, {z}')
# print(f'a is {z}, {y}, {x}')

# name = 'Jun'
# family = 'Sakai'
# print(f'My name is {name} {family}. Watashi ha {family} {name}')

'''
    辞書型
'''
# d = {
#     'x': 100,
#     'y': 200
# }
# for key,value in d.items():
#     print(key, ':', value)


def raise_function(a, b):
    try:
        a/b
    except:
        print("raise_function")
        raise


try:
    raise_function(a=1, b=0)
    raise_function(b=1, a=0
                   )
except Exception as e:
    # import traceback
    # print(traceback.print_exc())
    print("Exception : " + repr(e))
finally:
    print('処理終了')
