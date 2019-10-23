import re


def get_address(port):
    f = open('file.txt')
    while True:
        data = ''
        for line in f:
            if line == "":
                break
            data += line
        if not data:
            return "没有端口数据"
    obj = re.match(r'\S+', data)
    if port == obj.group():
        pattern = r'(\d{1,3}\.){3}\d{1,3}/\d{2}|unknown)'
        obj = re.search(pattern, data)
        if obj:
            return obj.group()


if __name__ == '__main__':
    port = input('请输入端口:')
    print(get_address(port))
