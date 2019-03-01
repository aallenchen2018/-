#coding=utf-8
import pymongo
conn=pymongo.MongoClient(host='127.0.0.1',port=27017)
db=conn.toto  #名字叫toto的数据库, 下面建立一个叫做jianli的表格
# db.jianli.insert([{'name':'wuyi','tel':566787,'exp':3},{'name':'kangshao','tel':2256677,'exp':0},{'name':'dabiaoge','tel':44997990,'exp':3}])


while 1:
	

	chose=input('1-查询;2-增加:3-删减;4-更新;5-预览表格')
	#查询
	if chose =='1':
		chosefind=input('name?')
		namefind=db.jianli.find({'name':chosefind},{'_id':0})
		for i in namefind:
			print(i)
	#增加
	elif chose=='2':
		add=input('name?')
		check=db.jianli.find({'name':add})
		if check.count()==0:
			add_tel=int(input('tel'))
			add_exp=int(input('exp'))
			db.jianli.insert({'name':add,'tel':add_tel,'exp':add_exp})
			
		else:
			print('此名字已有')


	#删减
	elif chose=='3':
		del_chose=input('1.删除一列数据;2.删除一个数据')
		if del_chose=='1':	
			del2=input('name')
			check=db.jianli.find({'name':del2})
			if check.count()==0:
				print('name not exists')
				
			else:
				db.jianli.remove({'name':del2})
				
		elif del_chose=='2':
			del3=input('name')
			choose_del=input('1.删除tel;2.删除exp')
			check=db.jianli.find({'name':del3})
			if check.count()==0:
				print('name not exists')
				
			else:
				if choose_del=='1':
					find_tel=db.jianli.find({'name':del3},{'tel':1,'_id':0})
					print(find_tel)
					for i in find_tel:
						global tel_value
						tel_value=i['tel']
						print(tel_value)
					db.jianli.update({'name':del3},{'$unset':{'tel':tel_value}})
				else:
					find_exp=db.jianli.find({'name':del3},{'exp':1,'_id':0})
					print(find_exp)
					for i in find_exp:
						global exp_value
						exp_value=i['exp']
						print(exp_value)
					db.jianli.update({'name':del3},{'$unset':{'exp':exp_value}})

		



	#修改
	elif chose=='4':
		update_name=input('update name?')
		update_tel=int(input('update tel?'))
		update_exp=int(input('update exp?'))	
		db.jianli.update({'name':update_name},{'$set':{'tel':update_tel,'exp':update_exp}})
	#阅览
	elif chose=='5':
		阅览=db.jianli.find({},{'_id':0})
		for i in 阅览:
			print(i)
	else:
		print('please chose between 1-5')
