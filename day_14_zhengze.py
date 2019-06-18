# import re
# # # s = "赵丽颖：1987，古力娜扎：1992"
# # # a =re.findall("\d+",s)
# # # print(a)
# #
# # s = "Alex:1994,Sunny:1993"
# # pattern = r"(\w+):(\d+)"
# # l = re.findall(pattern,s)
# # print(l)
# #使用compile对象调用
# # regex = re.compile(pattern)
# # l = regex.findall(s)#(s)
# # print(l)
#
# #按照匹配内容切割字符串
# # l = re.split(r"[:,]",s)
# # print(l)
#
# #替换匹配到的内容
# # a = re.sub(r"\s+","#","this is a shit",2)
# # print(a)
#
# # a = re.subn(r"\s+","#","this is a shit",2)
# # print(a)
# #联系
# """
# 提取出一段文字的日期（２０１９－０５－２３）
# 将日期打印出来，打印格式为２０１９／０５／２３
# """
#
# # st = "2008-08-09北京奥运会" \
# #     "2008-5-12汶川地震" \
# #     "2008-10-01国庆节"
# # b = re.sub(r"\－+","/","２０１９－０５－２３")
# # print(b)
#
# """
# regex1实例
# """
# # import re
# # s = "2019年，建国70年"
# # pattern = r"\d+"
# # # 返回迭代器
# # it  = re.finditer(pattern,s)
# # for i in it:
# #     print(i)
# # it  = re.finditer(pattern,s)
# # for i in it:
# #     print(i.group())
#
#
# #完全匹配
# # m =re.fullmatch(r"\w+","jame-1")
# # print(m)
#
# #匹配开始位置
# # import re
# # d = re.match(r"[A-Z]\W*","Hello Word")
# # print(d)
# #匹配第一处
# # import re
# # c = re.search(r"[A-Z]\W*"," Hello Word")#注意空格
# # print(c)
#
#
# #match对象示例
# # import re
# # pattern = r"(ab)cd(?P<pig>ef)"
# # regex = re.compile(pattern)
# # obj = regex.search("abcdefghi")#match对象
# # #属性变量、、
# # print(obj.pos)#目标字符串开头位置
# # print(obj.endpos)#目标字符串结尾位置
# # print(obj.re)#正则
# # print(obj.string)#目标字符串
# # print(obj.lastgroup)#最后一组组名
# # print(obj.lastindex)#最后一组序列号
# #
# # #属性方法
# # print(obj.span())#匹配内容在目标字符串位置/获取匹配内容的起止位置#。。。。。。。。。。。常用
# # print(obj.start())#
# # print(obj.end())#
# # print(obj.groupdict())#获取捕获组字典,组名为键,对应内容为值
# # print(obj.groups())#子组内容
# # print(obj.group(2))#常用。。。。。。。。。。。。。。＃获取第二个子组
# # #flagsｋｕｏｚｈａｎｇｏｎｇｎ展示
# # import re
# # q = """Hello
# # 北京
# # """
# #只能匹配ASCII
# # regex = re.compile(r"\w+",flags=re.A)
# #不区分到小写
# # regex = re.compile(r"[a-z]+",flags=re.I)
# #使.可以匹配换行
# # regex = re.compile(r".+",flags=re.S)
# #^$匹配每行开头结尾
# # regex = re.compile(r"^北京",flags=re.M)
# #添加注释
# # pattern = """\W+ #HALLO
# # """
# # regex = re.compile(pattern,flags=re.X)
# # l =regex.findall(q)
# # print(l)
#
# #熟练掌握元字符的使用
# #re模块函数
# #通过分析文档使用正则文档完成接口编写
# """
# 提取出一段文字的日期（２０１９－０５－２３）
# 将日期打印出来，打印格式为２０１９／０５／２３
# # b = re.sub(r"\－+","/","２０１９－０５－２３")
# """
#
# import re
# #
# s = """2008-08-08北京奥运会,
# 2008-05-12汶川地震,
# 2019-10-01建国70周年
# """
# # pattern = r"\d{4}-\d{2}-\d{2}"
# # l = re.findall(pattern,s)
# # # print(l)
# # b = re.sub(r"-+","/",str(l))
# # print(b)
#
#
#
#
# # pattern = r"\d{4}-\d{2}-\d{2}"
# # l = re.findall(pattern,s)
# #
# # for i in l:
# #   print(re.sub(r'-','/',i))
# """
# 1.字符串
# ２．正则模式
# 3.变量　＝　re.findall(字符串，正则模式)
# """
#
# """
# 1.[字符集]
#     [abc#!好] 表示 [] 中的任意一个字符
#     [0-9],[a-z],[A-Z] 表示区间内的任意一个字符
#     [_#?0-9a-z] 混合书写,一般区间表达写在后面
#     In : re.findall('[aeiou]',"How are you!")
#     Out: ['o', 'a', 'e', 'o', 'u']
# 2.[^字符集]
#     匹配除了字符集以外的任意一个字符
#     In : re.findall('[^0-9]',"Use 007 port")
#     Out: ['U', 's', 'e', ' ', ' ', 'p', 'o', 'r', 't']
# 3.^
#     匹配目标字符串的开头位置
#     In : re.findall('^Jame',"Jame,hello")
#     Out: ['Jame']
# 4.$
#     匹配目标字符串的结尾位置
#     In : re.findall('Jame$',"Hi,Jame")
#     Out: ['Jame']
# 5.*
#     匹配前面的字符出现0次或多次
#     In : re.findall('wo*',"wooooo~~w!")
#     Out: ['wooooo', 'w']
# 6.+
#     匹配前面的字符出现1次或多次
#     In : re.findall('[A-Z][a-z]+',"Hello World")
#     Out: ['Hello', 'World']
# 7.?
#     匹配前面的字符出现0次或1次
#     In [28]: re.findall('-?[0-9]+',"Jame,age:18, -26")
#     Out[28]: ['18', '-26']
# 8.{n}
#     匹配前面的字符出现n次
#     In : re.findall('1[0-9]{10}',"Jame:13886495728")
#     Out: ['13886495728']
# 9.{m,n}
#     匹配前面的字符出现m-n次
#     In : re.findall('[1-9][0-9]{5,10}',"Baron:1259296994")
#     Out: ['1259296994']
# 10.\d \D
#     \d 匹配任意数字字符,\D 匹配任意非数字字符
#     In : re.findall('\d{1,5}',"Mysql: 3306, http:80")
#     Out: ['3306', '80']
# 11.\w \W
#     匹配规则: \w 匹配普通字符,\W 匹配非普通字符
#     说明: 普通字符指数字,字母,下划线,汉字。
#     In : re.findall('\w+',"server_port = 8888")
#     Out: ['server_port', '8888']
# 12.\s \S
#     匹配规则: \s 匹配空字符,\S 匹配非空字符
#     说明:空字符指 空格 \r \n \t \v \f 字符
#     In : re.findall('\w+\s+\w+',"hello   world")
#     Out: ['hello world")
# 13.\A \Z
#     匹配规则: \A 表示开头位置,\Z 表示结尾位置
# 14.\b \B
#     匹配规则: \b 表示单词边界,\B 表示非单词边界
#     说明:单词边界指数字字母(汉字)下划线与其他字符的交界位置
#     In : re.findall(r'\bis\b',"This is a test.")
#     Out: ['is']
#
# 1.正则表达式的转义
#   1. 如果使用正则表达式匹配特殊字符则需要加 \ 表示转义。
#   特殊字符: . * + ? ^ $ [] () {} | \
# 2.
#
# """
#
# # homework_exercise
# #通过分析文档使用正则完成接口编写.从终端输入端口名返回address地址
# # s = "Alex:1994,Sunny:1993"
# # pattern = r"(\w+):(\d+)"
# # import re
# # port = input("输入端口")
# # f = open("exc.txt","r")
# #
# # #找到port所在段
# # while True:
# #     for line in f:
# #         if line == "^$":
#
#
# # import re
# # f = open("exc.txt","r")
# # port = input("请输入端口号：")
# # while True:
# #     data =""
# #     for line in f:
# #         if line != "\n":
# #             data += line
# #
# #         else:
# #             break
# #
# #     if not data:
# #         break
# #     port_name = re.match(port,data)
# #     if port_name == port:
# #         address = re.search(r"(\d{1,3}\.){3}\d{1,3}/\d+|Unknown",data).group()
# #         print(address)
#
#
#
# # import re
# #
# # port = input("端口:")
# # f = open('exc.txt')
# #
# # # 找到port所在段
# # while True:
# #   data = ''
# #   for line in f:
# #     if line != '\n':
# #       data += line
# #     else:
# #       break
# #
# #   # 结尾退出循环
# #   if not data:
# #     print("没有这个端口")
# #     break
# #
# #   result = re.match(port,data)
# #   if result:
# #     # pattern = r'[0-9a-f]{4}\.[0-9a-f]{4}\.[0-9a-f]{4}'
# #     pattern = r"(\d{1,3}\.){3}\d{1,3}/\d+|Unknown"
# #     try:
# #       address = re.search(pattern,data).group()
# #       print(address)
# #     except:
# #       print("No address")
# #     break
#
# # c=(r"^[1 - 9]*[1 - 9][0 - 9]*$")
#
#　快排 low 第一个数序列号　high 最后一个数序列号






































