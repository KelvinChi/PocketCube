from core_mathmatic_encode import Cube


if __name__ == '__main__':
    # 下边两是句是用来得到本地文件的
    # make_file = Cube()
    # make_file.make_file()

    # horn_start = 'G97LJ6CI'
    def translate_formulee(string):
        if string == 'q':
            return 'q'
        lis = []
        result = []
        for i in range(len(string) // 2):
            lis.append(string[2 * i: 2 * i + 2])
        for j in lis:
            result.append(horn_dict_reversed[j])
        return ''.join(result)

    horn_dict_reversed = {'10': '1', '20': '2', '30': '3', '40': '4', '50': '5', '60': '6',
                          '70': '7', '80': '8', '11': '9', '21': 'A', '31': 'B', '41': 'C',
                          '51': 'D', '61': 'E', '71': 'F', '81': 'G', '12': 'H', '22': 'I',
                          '32': 'J', '42': 'K', '52': 'L', '62': 'M', '72': 'N', '82': 'O'}

    get_it = Cube()
    get_it.loading_dict()
    horn_start = translate_formulee(input('请输入魔方状态，例如：4010203050607080，按q退出：\n'))
    while horn_start != 'q':
        get_it.get_it(horn_start)
        horn_start = translate_formulee(input('请输入下一状态，如不需要则q退出：\n'))
    print('感谢使用~')