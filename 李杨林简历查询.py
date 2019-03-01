#coding=utf-8
import pymongo
conn=pymongo.MongoClient(host='127.0.0.1',port=27017)
db=conn.local
a=db.jianli.find()
for b in a:
	print(b)
while 1:
	choice=input('请输入你的选择，1为新增，2为修改，3为删除，4为查看,q退出')
	if choice=='1':
		name=input('请输入你的姓名')
		tel=input('请输入你的电话')
		age=input('请输入你的年龄')
		id1=input('请输入你的id')
		db.jianli.insert({'_id':id1,'tel':tel,'age':age,'name':name})
		print('输入完毕')
		data=db.jianli.find()
		for i in data:
			print(i)
	elif choice=='3':
		name=input('请输入你需要删除的姓名')
		db.jianli.remove({'name':name})
		print('删除成功')
		data=db.jianli.find()
		for i in data:
			print(i)
	elif choice=='2':
		xuanze=input('请输入您需要选择修改的项目，1姓名，2电话，3年龄,4所有')
		if xuanze=='1':
			name=input('请输入你需要修改的姓名')
			name2=input('请输入修改后的姓名')
			db.jianli.update({'name':name},{'$set':{'name':name2}})
			print('姓名修改成功')
		elif xuanze=='2':
			tel=input('请输入你需要修改的电话')
			tel2=input('请输入修改后的电话')
			print('tel修改成功')
			db.jianli.update({'tel':tel},{'$set':{'tel':tel2}})
		elif xuanze=='3':
			age=input('请输入你的年龄')
			age2=input('请输入修改后的年龄')
			db.jianli.update({'age':age},{'$ste':{'age':age2}})
			print('年龄修改成功')	
		elif xuanze=='4':
			name4=input('请输入需修改人的姓名')
			age3=input('请输入修改后的年龄')
			tel3=input('请输入修改后的电话')
			db.jianli.update({'name':name4},{'$set':{'age':age3,'tel':tel3}})
			data=db.jianli.find()
			for i in data:
				print(i)
	elif choice=='4':
		id1=input('请输入需要查询打ID：')
		db.jianli.find({'_id':id1})
		print('查询成功')
		data=db.jianli.find({'_id':id1})
		for j in data:
			print(j)
	elif choice=='q':
		print('退出')
		break
	else:
		print('无此选项')

