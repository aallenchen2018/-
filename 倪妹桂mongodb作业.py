#coding=utf-8
import pymongo
conn=pymongo.MongoClient(host='127.0.0.1',port=27017)
db=conn.test
while 1:
	type1=input('''
	增加请按1
	删除请按2
	修改请按3
	查询请按4
	退出请按5
	请输入您的操作：''')
	if type1=='1':
		name=input('请输入您的名字:')
		tel=input('请输入您的电话:')
		exp=input('请输入您的工作经历:')
		remind=input('确认信息无误输入:')
		if remind=='yes':
			db.resume.insert({'name':name,'tel':tel,'exp':exp})
		elif remind=='quit':
			break
		else:
			print('请重新输入信息')
	elif type1=='2':
		ch=input('''
		按照名字删除请按a
		按照电话删除请按b
		按照工作经历请按c
		请输入您的操作：''')
		if ch=='a':
			name=input('请输入您的名字:')
			db.resume.remove({'name':name})
		elif ch=='b':
			tel=input('请输入您的电话:')
			db.resume.remove({'tel':tel})
		elif ch=='c':
			exp=input('请输入您的工作经历:')
			db.resume.remove({'exp':exp})
			print('删除成功')
		else:
			print('输入有误')
	elif type1=='3':
		ch=input('''
		按照名字修改请按a
		按照电话修改请按b
		按照经历修改请按c
		请输入您的操作：''')
		if ch=='a':
			name=input('请输入您的名字:')
			ename=input('请输入您修改的名字')
			db.resume.update({'name':name},{'$set':{'name':ename}})
		elif ch=='b':
			tel=input('请输入您的电话:')
			etel=input('请输入您修改的电话')
			db.resume.update({'tel':tel},{'$set':{'tel':etel}})
		elif ch=='c':
			exp=input('请输入您的工作经历:')
			exprience=input('请输入您修改的经历')
			db.resume.update({'exp':exp},{'$set':{'exp':exprience}})
		else:
			print('输入有误')
	elif type=='4':
		ch=inpit('''
		按照名字查询请按a
		按照电话查询请按b
		按照经历查询请按c
		请输入您的操作：''')
		if ch=='a':
			name=input('请输入您的名字:')
			db.resume.find({'name':name})
		elif ch=='b':
			tel=input('请输入您的电话:')
			db.resume.find({'tel':tel})
		elif ch=='c':
			db.resume.find({'exp':exp})
		else:
			print('输入有误')
	elif type=='5':
		pirnt('已退出')
		break
	else:
		print('输入有误')
