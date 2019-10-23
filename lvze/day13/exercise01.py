import re


def get_address(port):
    f = open('exc.txt')
    while True:
        data = ""
        for line in f:
            if line == "\n":
                break
            data += line
        if not data:
            return "无数据端口"
        obj = re.match(r'\S+', data)
        if port == obj.group():
            pattern = r'(\d{1,3}\.){3}\d{1,3}/\d{2}|Unknown'
            obj = re.search(pattern, data)
            if obj:
                return obj.group()


if __name__ == '__main__':
    port = input("端口:")
    print(get_address(port))
TINYINT
