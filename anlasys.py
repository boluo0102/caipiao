import decimal

T = tuple()


def prize_number():  # 将txt中字符串转换为可运行的python语句
    l = []
    with open('prize_number.txt', 'r') as p:
        s = p.read().split('\n')
        for e in s:
            y = eval(e)
            l.append(y)
    return l


def switch(old):  # 将每个元组中的字符串转换为整数
    new = []
    for e in old:
        e = int(e)
        new.append(e)
    return new


def all_switch(useless):  # 转换整个列表
    useful = [switch(e) for e in useless]
    return useful


string = prize_number()
integer = all_switch(string)  # 最终可计算得列表

decimal.getcontext().prec = 4


def position(integer, index, number):  # 在位置index上数字number出现的概率
    p = tuple([e[index] for e in integer])
    l = decimal.Decimal(len(p))
    n = decimal.Decimal(p.count(number))
    probability = (n / l)
    return probability

def sequence(dictionary):  # 按数字顺序显示概率
    ks = [i for i in range(1,34)]
    a = ''
    for key in ks:
        key = str(key)
        value = dictionary[key]
        if value != 0:
            a += key + '-->>' + str(dictionary[key]) + '\n'
    return a


def all_number(integer, index):  # 在位置index上所有数字出现的概率
    d = {}
    for i in range(1, 34):
        p = position(integer, index, i)
        k = str(i)
        d[k] = p
    return d


def all_position(integer):  # 在所有位置上所有数字出现的概率
    export = ''
    for i in range(7):
        k_n = all_number(integer, i)
        if i != 6:
            i += 1
        elif i == 6:
            i = '特殊'
        guide = str(i) + '位置上的数字'
        export += guide + '\n' + sequence(k_n) + '=========================\n'
    return export


def save(file,export):
    with open(file, 'a') as w:
        w.write(export)


if __name__ == '__main__':
    save('probability.txt',all_position(integer))