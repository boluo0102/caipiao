import re
import urllib.request as u


def save(items):  # 以一组数据一行的格式保存数据到txt中
    for item in items:
        s_item = str(item)
        with open('prize_number.txt', 'a') as w:
            w.write(s_item + '\n')


def get_url(page=104):  # 用列表装入所有需要爬的网页
    all_url = ['http://kaijiang.zhcw.com/zhcw/html/ssq/list_'
               + str(i+1) + '.html' for i in range(page)]
    return all_url


def prize_number(page):  # 得到所有数据,参数是网页的页数
    number = []
    url = get_url(page)
    pattern = re.compile('<td align="center" style=.*?' +
                         '<em class="rr">(.*?)<.*?' * 6 +
                         '<em>(.*?)</em></td>', re.S)
    for e in url:
        response = u.urlopen(e)
        content = response.read().decode('utf-8')
        items = re.findall(pattern, content)
        number.append(items)
        # save(items)
    return number


if __name__ == '__main__':
    print(prize_number(104))