#!/usr/bin/env python3
# _*_ coding:utf-8 _*_


def count(step):
    a = 126
    a = a * 11 - 66
    b = 1458
    for i in range(step - 3):  # 20步对应为17的range值
        a = a * 11 - 72 * 10 * (11 ** i)
        b += a
        print(i + 4, a)
    print('运行%s步' % step, '总类数：%.3e个' % b, sep='\n')
    print('运行%s步需要占用硬盘' %
          step, str('%.3e' %
                    ((20 * b) / (1024**3))), 'GB', '\n')


s1 = 11
s2 = 20 - s1
count(s1)
count(s2)


def scale(num):
    # a = '1'
    a = 'BBABBABBABB'
    b = int(a, 12)
    temp = []
    while b > 0:
        temp.append(b % num)
        b //= num
    temp.reverse()
    print('进制数：%s' % num, '最终长度：%s' % len(temp))


num_list = [216, 210]
for i in num_list:
    scale(i)


final_string = '123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ' \
               'abcdefghijklmnopqrstuvwxyz!#$%&()*+,' \
               '-.:;<=>?@[]^_`{|}~' \
               '¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ¶·¸¹º»¼½¾¿' \
               'ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâ' \
               'ãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿ\'"\\/'
print(len(set(final_string)))
# print(''.join(sorted(list(set(final_string)))))
# for i in range(100):
#     with open('ha.ck1', 'a', encoding='ISO-8859-1') as ck:
#         ck.write(final_string)

print('全部可编码数为：%s' % (len(set(final_string))))
for x in final_string:
    try:
        y = x.encode('ISO-8859-1')
        if len(y) == 1:
            pass
        else:
            print(x)
    except UnicodeEncodeError:
        print('无法编码', x)

# dict = {}
# num = 0
# for x in final_string:
#     dict[x] = num
#     num += 1
# print(dict)

amount = 4.3 * (10 ** 19)
print((amount * 20) / 8 / (1024 ** 6))

