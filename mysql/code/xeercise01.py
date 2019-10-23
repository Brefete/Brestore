
def store_message():
    while True:
        data = []
        id = int(input('id:'))
        name = input('Name:')
        passwd = int(input('Passwd:'))
        data.append((id,name,passwd))
        print(data)
store_message()
