# # import re
# # s = 'Alex:1994,Sunny:1996'
# # pattern = r"(\w+):(\d+)"
# #
# # l = re.findall(pattern,s)
# # print(l)
# #
# #
# # regex = re.compile(pattern,flags=0)
# # l = regex.findall(s,0,15)
# # print(l)
# #
#
# #
# import re
# s = '2019年10月1日举行了国庆阅兵，庆祝建国70周年。'
# pattern = r"\d+"
# r = re.finditer(pattern,s)
# # for i in r:
#     # print(i.group())
#
# m = re.fullmatch(r'.+',s)
# print(m.group())
#
# m = re.match(r'\w+',s)
# print(m.group())
#
# m = re.search(r'国+',s)
# print(m.group())
#
#
#
# import re
# s = """Hello
# 北京
# """
# regex = re.compile(r'Hello$',flags=re.M)
# l = regex.findall(s)
# print(l)



