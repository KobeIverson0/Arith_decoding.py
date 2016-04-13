#!/usr/bin/python
#-*-coding:utf8-*-

# 
#                                 _oo8oo_
#                                o8888888o
#                                88" . "88
#                                (| -_- |)
#                                0\  =  /0
#                              ___/'==='\___
#                            .' \\|     |// '.
#                           / \\|||  :  |||// \
#                          / _||||| -:- |||||_ \
#                         |   | \\\  -  /// |   |
#                          | \_|  ''\---/''  |_/ |
#                         \  .-\__  '-'  __/-.  /
#                       ___'. .'  /--.--\  '. .'___
#                    ."" '<  '.___\_<|>_/___.'  >' "".
#                    | | :  `- \`.:`\ _ /`:.`/ -`  : | |
#                   \  \ `-.   \_ __\ /__ _/   .-` /  /
#               =====`-.____`.___ \_____/ ___.`____.-`=====
#                                  `=---=`
#  
# 
#               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 
#                         佛祖保佑           永无bug
#




import re

fname = raw_input('enter the file name: ')

fhand = open(fname, 'r')

text = ''
for i in fhand:
	text = text + i


'''a = re.findall(r'\[(.*)\]', text)				#	提取字典
#a = a[0]'''

a_1 = text.index('[')
a = text[a_1 + 1: -1]

code = text[: a_1]

dictionary = {}
for i in a.split('  '):
	f = i.split(' ')
	if (f[0] == '\'' and f[1] == '\''):
		dictionary[' '] = [int(f[2]), int(f[3])]
	else:
		dictionary[f[0]] = [int(f[1]), int(f[2])]
	#dictionary[f[0]] = [int(f[1]), int(f[2])]	#	提取字典

'''dr = re.compile(r'\[.*\]', re.S)
code = dr.sub('', text)							#	提取编码部分
'''


length = 0
for i in dictionary:
	if dictionary[i][1] > length:
		length = dictionary[i][1]				#	提取 text 总长度

head = ''										#	dictionary[head][0] == 0
for i in dictionary:
	if dictionary[i][1] == length:
		head = i

x = code.index('.')
m = int(code[: x])								#	m = 编码位数
code = code[x + 1: ]

l = 0
u = 2 ** m - 1
k = 0											#	k 为已经读取的位数
t = code[: m]									#	初始化 l u k t
res = ''
target = ''

while len(res) < length:
	index = ((int(t, 2) - l + 1) * length - 1) / (u - l  + 1)

	#print index

	if index == length:
		target = head
		res = res + target
	else:
		for i in dictionary:
			if index >= dictionary[i][0] and index < dictionary[i][1]:
				target = i
				res = res + target

	
	#print target

	l , u = l + (u - l + 1) * dictionary[target][0] / length, l + (u - l + 1) * dictionary[target][1] / length - 1
	l = '0' * (m + 2 - len(bin(l))) + bin(l)[2: ]
	u = '0' * (m + 2 - len(bin(u))) + bin(u)[2: ]
	t = '0' * (m - len(t)) + t
	
	#print l, u, int(l, 2), int(u, 2), t, int(t, 2), res

	while(l[0] == u[0] or (l[: 2] == '01' and u[: 2] == '10')):
		if l[0] == u[0]:
			l = l[1: ] + '0'
			u = u[1: ] + '1'
			t = t[1: ] + code[k + m]
			k = k + 1
			
			#print l, u, int(l, 2), int(u, 2), t, int(t, 2), res

		else:
			l = '0' + l[2: ] + '0'
			u = '1' + u[2: ] + '1'
			t = t[1: ] + code[k + m]
			k = k + 1
			b = int(t[0])
			t = str(b ^ 1) + t[1: ]

			#print l, u, int(l, 2), int(u, 2), t, int(t, 2), res

	l = int(l, 2)
	u = int(u, 2)

#print res
ffhand_name = fname[: -9] + '_decode.txt'
print ffhand_name
ffhand = open(ffhand_name, 'w')
ffhand.write(res)
ffhand.close()
print 'Done!'







