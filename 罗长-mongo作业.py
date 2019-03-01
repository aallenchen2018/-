#coding=utf-8
import pymongo
conn=pymongo.MongoClient(host='127.0.0.1',port=27017)
db=conn.test1
def Add():
	name,number,jingli='null','null','null'
	name=input('请输入你的名字:')
	number=input('请输入你的电话:')
	jingli=input('请输入你的经历:')
	db.jianli.insert({'name':name,'number':number,'jingli':jingli})
def upat():
	while True:
		a=0
		print('''
	查看已录入的的简历信息：
	输入1,修改电话号码
	输入2,修改经历
	输入3,退出修改
	''')
		b=int(input())
		if b==1:
			name1=input('输入你的名字:')
			data=db.jianli.find({})
			a=[x for x in data if name1==x['name']]
			if len(a)==0:
				print('名字不存在！')
			else:
				number1=input('修改的电话:')
				db.jianli.update({'name':name1},{'$set':{'number':number1}})
				print('修改成功')
		elif b==2:
			name1=input('输入你的名字:')
			data=db.jianli.find({})
			a=[x for x in data if name1==x['name']]
			if len(a)==0:
				print('名字不存在！')
			else:
				jingli1=input('修改的经历:')
				db.jianli.update({'name':name1},{'$set':{'jingli':jingli1}})
				print('修改成功')
		elif b==3:
			print('退出成功')
			break
		else:
			print('输入错误!')
def Del():
	name=input('请输入删除行的名字:')
	db.jianli.remove({'name':name})
def look():
	while True:
		print('''
	查看已录入的的简历信息：
	输入1,按照名字进行查询
	输入2,按照电话号码进行查询
	输入3,按照经历进行查询
	输入4,退出查询
	''')
		c=int(input())
		if c==1:
			name2_1=input('请输入名字:')
			data=db.jianli.find({})
			a=[x for x in data if name2_1==x['name']]
			if len(a)==0:
				print('名字不存在！')
			else:
				test=db.jianli.find({'name':name2_1},{'_id':0})
				for i in test:
					print(i)
		elif c==2:
			name2_2=input('请输入电话号码:')
			data=db.jianli.find({})
			a=[x for x in data if name2_2==x['name']]
			if len(a)==0:
				print('电话号码不存在！')
			else:
				test=db.jianli.find({'number':name2_2},{'_id':0})
				for i in test:
					print(i)
		elif c==3:
			name2_3=input('请输入经历:')
			data=db.jianli.find({})
			a=[x for x in data if name2_3==x['name']]
			if len(a)==0:
				print('经历不存在！')
			else:
				test=db.jianli.find({'jingli':name2_3},{'_id':0})
				for i in test:
					print(i)
		elif c==4:
			print('退出成功')
			break
		else:
			print('输入错误')
while True:
	a=int(input("增加,修改，删除，查看,退出(1,2,3,4,5):"))
	if a==1:
		Add()
	elif a==2:
		upat()
	elif a==3:
		Del()
	elif a==4:
		look()
	elif a==5:
		print('退出成功')
		break
	else:
		print('输入错误')
