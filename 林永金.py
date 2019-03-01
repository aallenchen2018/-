#coding=utf-8
import pymongo
conn=pymongo.MongoClient(host='127.0.0.1',port=27017)
db=conn.jianli

def find1():
	tcho=input('''
	查询所有文档请按a
	根据名字查询文档请按b
	根据电话查询文档请按c
	根据经历查询文档请按d
	返回上一层按q
				''')                        
	if tcho=='a':
		data=db.jianli.find({},{'_id':0})
		for i in data:
			print('名字:'+i['name']+'  电话:'+i['num']+'  经历:'+i['exp'])
	elif tcho=='b':
		ename=input('请输入名字: ')
		data=db.jianli.find({'name':ename},{'_id':0})
		for i in data:
			print('名字:'+i['name']+'  电话:'+i['num']+'  经历:'+i['exp'])
	elif tcho=='c':
		enum=input('请输入电话: ')
		data=db.jianli.find({'num':enum},{'_id':0})
		for i in data:
			print('名字:'+i['name']+'  电话:'+i['num']+'  经历:'+i['exp'])
	elif tcho=='d':
		eexp=input('请输入经历: ')
		data=db.jianli.find({'exp':eexp},{'_id':0})
		for i in data:
			print('名字:'+i['name']+'  电话:'+i['num']+'  经历:'+i['exp'])
	elif tcho=='q':
		pass
	else:
		print('输入有误')

def del1():
	tcho=input('''
	根据名字删除文档请按a
	根据电话删除文档请按b
	根据经历删除文档请按c
	返回上一层按q
				''')
	if tcho=='a':
		while 1:
			ename=input('请输入名字: ')
			data=db.jianli.find({'name':ename})
			if data.count()==0:
				t=input('''
	名字不存在
	请重新输入
	任意键继续
	q键退出
					''')
				if t=='q':
					break
				else:
					continue
	
			else:
				db.jianli.remove({'name':ename})
				print('删除成功')
				break
	elif tcho=='b':
		while 1:
			enum=input('请输入号码: ')
			data=db.jianli.find({'num':enum})
			if data.count()==0:
				t=input('''
	号码不存在
	请重新输入
	任意键继续
	q键退出
				''')
				if t=='q':
					break
				else:
					continue
			else:
				db.jianli.remove({'num':enum})
				print('删除成功')
	elif tcho=='c':
		while 1:
			eexp=input('请输入经历: ')
			data=db.jianli.find({'exp':eexp})
			if data.count()==0:
				t=input('''
	经历不存在
	请重新输入
	任意键继续
	q键退出
				''')
				if t=='q':
					break
				else:
					continue
			else:
				db.jianli.remove({'exp':eexp})
				print('删除成功')
	elif tcho=='q':
		pass
	else:
		print('输入有误')
def update1():
	while 1:
		ename=input('请输入名字: ')
		data=db.jianli.find({'name':ename})
		if data.count()==0:
			t=input('''
	名字不存在
	请重新输入
	任意键继续
	q键退出
				''')
			if t=='q':
				break
			else:
				continue
		else:
			enum=input('请输入修改电话: ')
			eexp=input('请输入修改经历: ')
			db.jianli.update({'name':ename},{'$set':{'num':enum}})
			db.jianli.update({'name':ename},{'$set':{'exp':eexp}})
			print('修改成功')
			break

def ins1():
	while 1:
		ename=input('请输入名字: ')
		enum=input('请输入号码: ')
		eexp=input('请输入经历: ')
		tcho2=input('确认信息请按yes\n任意键重输\nq键退出')
		if tcho2=='yes':
			db.jianli.insert({'name':ename,'num':enum,'exp':eexp})
			print('增加成功')
			break
		elif tcho2=='q':
			break
		else:
			continue

while 1:

	type1=input('''
	查询请按1
	删除请按2
	增加请按3
	修改请按4
	退出请按5
				''')

	if type1=='1':
		find1()
	elif type1=='2':
		del1()
	elif type1=='3':
		ins1()
	elif type1=='4':
		update1()
	elif type1=='5':
		break
	else:
		print('输入有误')	


