#!/usr/bin/env python3
# encoding: utf-8


# 角块方向判别加法
class Horn_adding:
    def __init__(self, str):
        self.str = str

    def __add__(self, other):
        global horn_dict, horn_dict_reversed
        num = horn_dict[self.str]
        if (num + other) % 10 == 3:
            return horn_dict_reversed[str((num // 10) * 10)]
        elif (num + other) % 10 == 4:
            return horn_dict_reversed[str((num // 10) * 10 + 1)]
        else:
            return horn_dict_reversed[str(num + other)]


# 棱块方向差别方法
class Edge_adding:
    def __init__(self, str):
        self.str = str

    def __add__(self, other):
        global edge_dict, edge_dict_reversed
        num = edge_dict[self.str]
        if (num + other) % 10 == 2:
            return edge_dict_reversed[str((num // 10) * 10)]
        else:
            return edge_dict_reversed[str(num + other)]


def judge(previous_steps, current_step):
    global moving
    if previous_steps == '':
        return True
    elif moving[previous_steps[-1]] + '\'' == moving[current_step] or \
            moving[previous_steps[-1]] == moving[current_step] + '\'':
        return False
    elif (previous_steps[-1] + current_step) in ['22', '44', '66', '88', 'AA', 'CC']:
        return False
    elif len(previous_steps) >=2 and len(set(previous_steps[-2:] + current_step)) == 1:
        return False
    else:
        return True


# def judge(steps):
#     global moving
#     if len(steps) == 1:
#         return True
#     elif len(steps) == 2 and moving[steps[-2]] + '\'' == moving[steps[-1]] or \
#             moving[steps[-2]] == moving[steps[-1]] + '\'':
#         return False
#     elif steps[-2:] in ['22', '44', '66', '88', 'AA', 'CC']:
#         return False
#     elif len(set(steps[-3:])) == 1:
#         return False
#     else:
#         return True


horn_dict = {'1': 10, '2': 20, '3': 30, '4': 40, '5': 50, '6': 60, '7': 70, '8': 80,
             '9': 11, 'A': 21, 'B': 31, 'C': 41, 'D': 51, 'E': 61, 'F': 71, 'G': 81,
             'H': 12, 'I': 22, 'J': 32, 'K': 42, 'L': 52, 'M': 62, 'N': 72, 'O': 82}
horn_dict_reversed = {'10': '1', '20': '2', '30': '3', '40': '4', '50': '5', '60': '6',
                      '70': '7', '80': '8', '11': '9', '21': 'A', '31': 'B', '41': 'C',
                      '51': 'D', '61': 'E', '71': 'F', '81': 'G', '12': 'H', '22': 'I',
                      '32': 'J', '42': 'K', '52': 'L', '62': 'M', '72': 'N', '82': 'O'}

edge_dict = {'1': 10, '2': 20, '3': 30, '4': 40, '5': 50, '6': 60, '7': 70, '8': 80,
             '9': 90, 'A': 100, 'B': 110, 'C': 120, 'D': 11, 'E': 21, 'F': 31, 'G': 41,
             'H': 51, 'I': 61, 'J': 71, 'K': 81, 'L': 91, 'M': 101, 'N': 111, 'O': 121}
edge_dict_reversed = {'10': '1', '20': '2', '30': '3', '40': '4', '50': '5', '60': '6',
                      '70': '7', '80': '8', '90': '9', '100': 'A', '110': 'B', '120': 'C',
                      '11': 'D', '21': 'E', '31': 'F', '41': 'G', '51': 'H', '61': 'I',
                      '71': 'J', '81': 'K', '91': 'L', '101': 'M', '111': 'N', '121': 'O'}

moving = {'1': 'U', '2': 'U\'', '3': 'D', '4': 'D\'', '5': 'R', '6': 'R\'',
          '7': 'L', '8': 'L\'', '9': 'F', 'A': 'F\'', 'B': 'B', 'C': 'B\''}
moving_reversed = {'U': '1', "U'": '2', 'D': '3', "D'": '4', 'R': '5', "R'": '6',
                   'L': '7', "L'": '8', 'F': '9', "F'": 'A', 'B': 'B', "B'": 'C'}


if __name__ == '__main__':
    print(Horn_adding('9') + 2)
