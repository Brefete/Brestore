import re


def get_address(port):
    f = open('exc.txt')
    data = ""
    for line in f:
        if line == '\n':
            break
        data += line
    if not data:
        return '没有端口'
    obj = re.match(r'\S+', data)
    if port == obj.group():
        obj = re.search(r'(\d{1,3}\.){3}\d{1,3}/\d{2}|Unknown', data)
        if obj:
            return obj.group()


if __name__ == '__main__':
    port = input('端口:')
    print(get_address(port))
