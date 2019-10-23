class User1:
    __slots__ = ['id', 'name', 'sex']
    def __init__(self, id, name, sex):
        self.id = id
        self.name = name
        self.sex = sex
u01 = User1(124,'yang','nan')
print(u01)
