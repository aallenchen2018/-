#coding=utf-8
import pymongo
conn=pymongo.MongoClient(host='127.0.0.1',port=27017)
db=conn.test
datacheck=db.xiyouji.find({},{'_id':0})
while 1:
	for i in datacheck:
		print(i)

	chose=input('1:search;2:add;3:dele;4update;5:type other you will quit:')
	if chose =='1':
		search1=input('search by:1:name;2:phone;3:exp')
		if search1=='1':
			search=input('name?')
			searchname=db.xiyouji.find({'name':search},{'_id':0})
			for i in searchname:
				print(i)
		elif search1=='2':
			search=input('phone?')
			searchphone=db.xiyouji.find({'phone':search},{'_id':0})
			for i in searchphone:
				print(i)
		elif search1=='3':
			search=input('exp?')
			searchexp=db.xiyouji.find({'exp':search},{'_id':0})
			for i in searchexp:
				print(i)
	elif chose=='2':
		add=input('name?')
		list1=[]
		read=db.xiyouji.find()
		for i in read:
			list1.append(i)
		if add in list1:
			print('name exist!')
		else:
			add1=int(input('tel?'))
			add2=int(input('exp?'))
			db.xiyouji.insert({'name':add,'tel':add1,'exp':add2})
	elif chose=='3':
		dele=input('name?')
		datacheck=db.xiyouji.find({'name':dele})
		if datacheck.count()!=0:
			db.xiyouji.remove({'name':dele})	
			print('dele sucess')
		else:
			print('not exist name.')
	
	elif chose=='4':
		update_name=input('update name?')
		update_tel=int(input('update tel?'))
		update_exp=int(input('update exp?'))	
		db.xiyouji.update({'name':update_name},{'$set':{'tel':update_tel,'exp':update_exp}})
	else:
		print('bye')
		break
