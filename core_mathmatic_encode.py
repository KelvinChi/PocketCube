#!/usr/bin/env python3
# _*_ coding:utf-8 _*_


import time, sys
from map import Horn_adding, judge
from decode_b import encode_bit, decode_bit
import re
import gc

class Cube:
    def __init__(self):
        self.dic = {}
        # 正向字典，用于生成还原公式
        self.moving_dict = {'1': 'U', '2': 'U\'', '3': 'D', '4': 'D\'', '5': 'R', '6': 'R\'',
                            '7': 'L', '8': 'L\'', '9': 'F', 'A': 'F\'', 'B': 'B', 'C': 'B\''}
        # 逆向字典，用于生成还原公式
        self.moving_back_dict = {'1': 'U\'', '2': 'U', '3': 'D\'', '4': 'D', '5': 'R\'', '6': 'R',
                                 '7': 'L\'', '8': 'L', '9': 'F\'', 'A': 'F', 'B': 'B\'', 'C': 'B'}

    @staticmethod
    def u(previous_steps, horn_status):
        if judge(previous_steps, '1'):
            horn = list(horn_status)
            horn_moved = [horn[3], horn[0], horn[1], horn[2],
                    horn[4], horn[5], horn[6], horn[7]]
            return previous_steps + '1', ''.join(horn_moved)
        return None

    @staticmethod
    def u_u(previous_steps, horn_status):
        if judge(previous_steps, '2'):
            horn = list(horn_status)
            horn_moved = [horn[1], horn[2], horn[3], horn[0],
                    horn[4], horn[5], horn[6], horn[7]]
            return previous_steps + '2', ''.join(horn_moved)
        return None

    @staticmethod
    def d(previous_steps, horn_status):
        if judge(previous_steps, '3'):
            horn = list(horn_status)
            horn_moved = [horn[0], horn[1], horn[2], horn[3],
                    horn[5], horn[6], horn[7], horn[4]]
            return previous_steps + '3', ''.join(horn_moved)
        return None

    @staticmethod
    def d_d(previous_steps, horn_status):
        if judge(previous_steps, '4'):
            horn = list(horn_status)
            horn_moved = [horn[0], horn[1], horn[2], horn[3],
                    horn[7], horn[4], horn[5], horn[6]]
            return previous_steps + '4', ''.join(horn_moved)
        return None

    @staticmethod
    def r(previous_steps, horn_status):
        if judge(previous_steps, '5'):
            horn = list(horn_status)
            horn_moved = [horn[0], horn[1], Horn_adding(horn[3]) + 2, Horn_adding(horn[7]) + 1,
                    horn[4], horn[5], Horn_adding(horn[2]) + 1, Horn_adding(horn[6]) + 2]
            return previous_steps + '5', ''.join(horn_moved)
        return None

    @staticmethod
    def r_r(previous_steps, horn_status):
        if judge(previous_steps, '6'):
            horn = list(horn_status)
            horn_moved = [horn[0], horn[1], Horn_adding(horn[6]) + 2, Horn_adding(horn[2]) + 1,
                    horn[4], horn[5], Horn_adding(horn[7]) + 1, Horn_adding(horn[3]) + 2]
            return previous_steps + '6', ''.join(horn_moved)
        return None

    @staticmethod
    def l(previous_steps, horn_status):
        if judge(previous_steps, '7'):
            horn = list(horn_status)
            horn_moved = [Horn_adding(horn[1]) + 2, Horn_adding(horn[5]) + 1, horn[2], horn[3],
                          Horn_adding(horn[0]) + 1, Horn_adding(horn[4]) + 2, horn[6], horn[7]]
            return previous_steps + '7', ''.join(horn_moved)
        return None

    @staticmethod
    def l_l(previous_steps, horn_status):
        if judge(previous_steps, '8'):
            horn = list(horn_status)
            horn_moved = [Horn_adding(horn[4]) + 2, Horn_adding(horn[0]) + 1, horn[2], horn[3],
                          Horn_adding(horn[5]) + 1, Horn_adding(horn[1]) + 2, horn[6], horn[7]]
            return previous_steps + '8', ''.join(horn_moved)
        return None

    @staticmethod
    def f(previous_steps, horn_status):
        if judge(previous_steps, '9'):
            horn = list(horn_status)
            horn_moved = [Horn_adding(horn[4]) + 1, horn[1], horn[2], Horn_adding(horn[0]) + 2,
                          Horn_adding(horn[7]) + 2, horn[5], horn[6], Horn_adding(horn[3]) + 1]
            return previous_steps + '9', ''.join(horn_moved)
        return None

    @staticmethod
    def f_f(previous_steps, horn_status):
        if judge(previous_steps, 'A'):
            horn = list(horn_status)
            horn_moved = [Horn_adding(horn[3]) + 1, horn[1], horn[2], Horn_adding(horn[7]) + 2,
                          Horn_adding(horn[0]) + 2, horn[5], horn[6], Horn_adding(horn[4]) + 1]
            return previous_steps + 'A', ''.join(horn_moved)
        return None

    @staticmethod
    def b(previous_steps, horn_status):
        if judge(previous_steps, 'B'):
            horn = list(horn_status)
            horn_moved = [horn[0], Horn_adding(horn[2]) + 2, Horn_adding(horn[6]) + 1, horn[3],
                    horn[4], Horn_adding(horn[1]) + 1, Horn_adding(horn[5]) + 2, horn[7]]
            return previous_steps + 'B', ''.join(horn_moved)
        return None

    @staticmethod
    def b_b(previous_steps, horn_status):
        if judge(previous_steps, 'C'):
            horn = list(horn_status)
            horn_moved = [horn[0], Horn_adding(horn[5]) + 2, Horn_adding(horn[1]) + 1, horn[3],
                    horn[4], Horn_adding(horn[6]) + 1, Horn_adding(horn[2]) + 2, horn[7]]
            return previous_steps + 'C', ''.join(horn_moved)
        return None

    def moving(self, previous_steps='', horn_status='12345678'):
        u = self.u(previous_steps, horn_status)
        u_u = self.u_u(previous_steps, horn_status)
        d = self.d(previous_steps, horn_status)
        d_d = self.d_d(previous_steps, horn_status)
        r = self.r(previous_steps, horn_status)
        r_r = self.r_r(previous_steps, horn_status)
        l = self.l(previous_steps, horn_status)
        l_l = self.l_l(previous_steps, horn_status)
        f = self.f(previous_steps, horn_status)
        f_f = self.f_f(previous_steps, horn_status)
        b = self.b(previous_steps, horn_status)
        b_b = self.b_b(previous_steps, horn_status)
        return u, u_u, d, d_d, r, r_r, l, l_l, f, f_f, b, b_b

    def loading_dict(self):
        with open('decode6.ck', 'r', encoding='ISO-8859-1') as ck:
            datebase = ck.read().split(' ')
        start = time.time()
        for i in datebase[:-1]:
            # 如果字典收有值，则直接后加解，否则新建
            try:
                self.dic[re.findall(r'0(.+)', i)[0]].append(re.findall(r'(.+)0', i)[0])
            except KeyError:
                self.dic[re.findall(r'0(.+)', i)[0]] = [re.findall(r'(.+)0', i)[0]]
        end = time.time()
        print('字典加载完成，耗时%.3f秒。' % (end - start)) # 此处往上都是加载已有字典

    def get_it(self, horn_start):
        if self.dic == {}:
            print('字典未加载…')
            return
        layer_limit = 1
        big_list = [('', horn_start)]
        temp = []
        count = 0
        start = time.time()
        while layer_limit <= 7:
            for x in big_list:
                if x:
                    try:
                        formulee_1 = x[0]
                        key = encode_bit(decode_bit(x[1], 24), 210)
                        solutions = []
                        for item in self.dic[key]:
                            solutions.append(encode_bit(decode_bit(item, 210), 12))
                        solutions.sort()
                        formulee_2 = ''.join(list(reversed(sorted(solutions)[0])))
                        result = self.decode_formulee(formulee_1, formulee_2)
                        print(result, '步数为%s步' % len([''.join(_) for _ in result
                                                      if _.isalpha()]))
                        end = time.time()
                        print('耗时%.3f秒' % (end - start))
                        return
                    except KeyError:
                        pass
                    next_steps = self.moving(previous_steps=x[0], horn_status=x[1])
                    temp.extend(next_steps)
                    count += 1
                else:
                    continue
            big_list = temp
            temp = []
            layer_limit += 1
        end = time.time()
        print('未找到对应解，判断为输入有问题，耗时%.3f秒' % (end - start))
        gc.collect()

    def make_file(self):
        # 下边这些数与实际计算有些许出入，需要优化
        amount = {1: 12, 2: 126, 3: 1320, 4: 13800, 5: 143880, 6: 1495560, 7: 15492840,
                  8: 159879720, 9: 1642720200, 10: 16794398280, 11: 170707617960}
        layer_limit = 1
        count_one_layer = 0
        count_all = 0
        big_list = [('', '12345678')]
        temp = [] # 用于中转列表，需要优化
        while layer_limit <= 6: # 限制最大执行层数
            start = time.time()
            for i in big_list:
                if i:
                    next_steps = self.moving(i[0], i[1])
                    temp.extend(next_steps)
                else:
                    continue
                for j in next_steps:
                    # 筛选函数为judge，见转动函数，前后不能形成RR'或不能连续三个RRR，且RR与R'R'只能存在RR
                    if j:
                        part_one = encode_bit(decode_bit(j[0], 12), 210)
                        part_two = encode_bit(decode_bit(j[1], 24), 210)
                        # part_one = j[0]
                        # part_two = j[1]
                        with open('decode6.ck', 'a', encoding='ISO-8859-1') as ck:
                            ck.write(part_one + '0' + part_two + ' ')
                        count_one_layer += 1
                        # 下边是进度条
                        sys.stdout.write("\r{0}{1}".format(">" * int(count_one_layer /
                                        amount[layer_limit] * 25), '%.2f%%' % int(count_one_layer
                                        / amount[layer_limit] * 100)))
                        sys.stdout.flush()
            big_list = temp
            temp = []
            end = time.time()
            count_all += count_one_layer
            count_one_layer = 0
            print('\n第%s层运行完成：' % layer_limit + '\n' +
                  '累计%s条数据，耗时%.3f秒' % (count_all, (end - start)))
            layer_limit += 1
            gc.collect()

    def decode_formulee(self, first, second):
        if first[-1] == second[0]:
            first = first[:-1]
            second = second[1:]
        result = []
        for i in first:
            result.append(self.moving_dict[i])
        for j in second:
            result.append(self.moving_back_dict[j])
        for x in range(len(result) - 1):
            try:
                if result[x] == result[x + 1] == result[x + 2]:
                    result[x + 1] = '0'
                    result[x + 2] = '0'
            except IndexError:
                pass
            if result[x] == result[x + 1] and result[x] != '0':
                result[x] = result[x][0]
                result[x + 1] = '2'
        return ''.join([x for x in result if x != '0'])


if __name__ == '__main__':
    # 下边两是句是用来得到本地文件的
    make_file = Cube()
    make_file.make_file()
    # horn_start = 'G97LJ6CI'
    # get_it = Cube()
    # get_it.loading_dict()
    # get_it.get_it(horn_start)
