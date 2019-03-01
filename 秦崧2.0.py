#coding=utf-8
import pymongo
class db_resume:
	def resume_add(self):
		conn=pymongo.MongoClient(host='127.0.0.1',port=27017)
		db=conn.resume
		while 1:
			id_1=0
			find_1 = db.resume.find({})
			print('读取id中...')
			for i in find_1:
				continue
			if len(i) > 1:
				id_1 = i['_id']+1
			else:
				id_1+=1
			name_1 = input('请输入您的名字: ')
			tel_1 = input('请输入您的电话: ')
			ex_1 = input('请输入您的工作经历: ')
			input_1 = input('确认信息输入(yes),退出请输入(quit),重新输入请输入(again): ')
			if input_1 == 'yes':	
				db.resume.insert({'_id':id_1,'name':name_1,'tel':tel_1,'ex':ex_1})
				print('添加一条数据成功')
				print('新增的数据为: id:'+str(id_1)+' 名字: '+name_1+' 电话: '+tel_1+' 经历: '+ex_1)
			elif input_1 == 'again':
				print('请重新输入: ')
			elif input_1 == 'quit':
				print('已退出新增!!')
				break
			else:
				print('选择错误,请重新输入!!')
	def resume_delete(self):
		conn=pymongo.MongoClient(host='127.0.0.1',port=27017)
		db=conn.resume
		while 1:
			print('''
			删除已经录入的简历信息:
			输入a,按照编号进行删除,
			输入b,按照名字进行删除,
			输入c,按照电话进行删除,
			输入d,按照经历进行删除,
			输入quit,退出.
			''')
			a = 0
			input_4 = input('请输入您的选择: ')
			if input_4 == 'a':
				id_1 = input('请输入您要删除数据的编号: ')
				data = db.resume.find({})
				for i in data:
					if i['_id'] == id_1:
						print('您删除的数据: 编号: '+str(i['_id'])+' 名字: '+i['name']+' 电话:'+i['tel']+' 经历:'+i['ex'])
						db.resume.remove({'_id':int(id_1)})
						print('删除数据成功')
					else:
						a = 1
				if a == 1:
					print('您要删除的编号不存在!!')
			elif input_4 == 'b':
				a = 0
				name_1 = input('请输入您要删除数据的名字: ')
				data = db.resume.find({})
				for i in data:
					if i['name'] == name_1:
						print('您删除的数据: 编号: '+str(i['_id'])+' 名字: '+i['name']+' 电话:'+i['tel']+' 经历:'+i['ex'])
						db.resume.remove({'name':name_1})
						print('删除数据成功')
					else:
						a = 1
				if a == 1:
					print('您要删除的名字不存在!!')
			elif input_4 == 'c':
				a = 0
				tel_1 = input('请输入您要删除数据的电话: ')
				data = db.resume.find({})
				for i in data:
					if i['tel'] == tel_1:
						print('您删除的数据: 编号: '+str(i['_id'])+' 名字: '+i['name']+' 电话:'+i['tel']+' 经历:'+i['ex'])
						db.resume.remove({'tel':tel_1})
						print('删除数据成功')
					else:
						a = 1
				if a == 1:
					print('您要删除的电话不存在!!')
			elif input_4 == 'd':
				a = 0
				ex_1 = input('请输入您要删除数据的经历: ')
				data = db.resume.find({})
				for i in data:
					if i['ex'] == ex_1:
						print('您删除的数据: 编号: '+str(i['_id'])+' 名字: '+i['name']+' 电话:'+i['tel']+' 经历:'+i['ex'])
						db.resume.remove({'ex':ex_1})
						print('删除数据成功')
					else:
						a = 1
				if a == 1:
					print('您要删除的经历不存在!!')
			elif input_4 == 'quit':
				print('已退出删除!!')
				break
			else:
				print('您选择的有误,请重新输入: ')
	def resume_update(self):
		conn=pymongo.MongoClient(host='127.0.0.1',port=27017)
		db=conn.resume
		while 1:
			print('''
			通过查询编号修改已经录入的简历信息:
			输入a,按照名字进行修改,
			输入b,按照电话进行修改,
			输入c,按照经历进行修改,
			输入quit,退出.
			''')
			input_4 = input('请输入您的选择: ')
			id_1=input('请输入您选择的编号: ')
			if input_4 == 'a':
				a = 0
				name_1 = input('请输入您要修改的数据的名字: ')
				data = db.resume.find({'_id':int(id_1)})
				for i in data:
					if i['name'] == name_1:
						print('您修改的原信息为: 编号: '+i['_id']+' 名字: '+i['name']+' 电话:'+i['tel']+' 经历:'+i['ex'])
						db.resume.update({'_id':int(id_1)},{'$set':{'name':name_1}})
						print('您修改的新信息为: 编号: '+i['_id']+' 名字: '+name_1+' 电话:'+i['tel']+' 经历:'+i['ex'])
						print('修改数据成功')
					else:
						a = 1
				if a == 1:
					print('您要修改的名字不存在!!或者编号不存在!!')
			elif input_4 == 'b':
				a = 0
				tel_1 = input('请输入您要修改的数据的电话: ')
				data = db.resume.find({'_id':int(id_1)})
				for i in data:
					if i['tel'] == tel_1:
						print('您修改的原信息为: 编号: '+i['_id']+' 名字: '+i['name']+' 电话:'+i['tel']+' 经历:'+i['ex'])
						db.resume.update({'_id':int(id_1)},{'$set':{'tel':tel_1}})
						print('您修改的新信息为: 编号: '+i['_id']+' 名字: '+i['name']+' 电话:'+tel_1+' 经历:'+i['ex'])
						print('修改数据成功')
					else:
						a = 1
				if a == 1:
					print('您要修改的电话不存在!!或者编号不存在!!')
			elif input_4 == 'c':
				a = 0
				ex_1 = input('请输入您要修改的数据的经历: ')
				data = db.resume.find({'_id':int(ex_1)})
				for i in data:	
					if i['ex'] == ex_1:	
						print('您修改的原信息为: 编号: '+i['_id']+' 名字: '+i['name']+' 电话:'+i['tel']+' 经历:'+i['ex'])
						db.resume.update({'_id':int(id_1)},{'$set':{'ex':ex_1}})
						print('您修改的原信息为: 编号: '+i['_id']+' 名字: '+i['name']+' 电话:'+i['tel']+' 经历:'+ex_1)
						print('修改数据成功')
					else:
						a = 1
				if a == 1:
					print('您要修改的经历不存在!!或者编号不存在!!')
			elif input_4 == 'quit':
				print('已退出修改!!')
				break
			else:
				print('您选择的有误,请重新输入: ')
	def resume_find(self):
		conn=pymongo.MongoClient(host='127.0.0.1',port=27017)
		db=conn.resume
		while 1:
			print('''
			查看已经录入的简历信息:
			输入a,按照编号进行查询,
			输入b,按照名字进行查询,
			输入c,按照电话进行查询,
			输入d,按照经历进行查询,
			输入quit,退出.
			''')
			input_4 = input('请输入您的选择: ')
			if input_4 == 'a':
				a = 0
				id_1 = input('请输入您查询的编号: ')
				data = db.resume.find({})
				for i in data:
					if i['_id'] == int(id_1):
						print('编号: '+i['_id']+' 名字: '+i['name']+' 电话:'+i['tel']+' 经历:'+i['ex'])
					else:
						a = 1
				if a == 1:
					print('您查询的编号不存在!!')
			elif input_4 == 'b':
				a = 0
				name_1 = input('请输入您查询的名字: ')
				data = db.resume.find({'name':name_1})
				for i in data:
					if i['name'] == name_1:
						print('编号: '+i['_id']+' 名字: '+i['name']+' 电话:'+i['tel']+' 经历:'+i['ex'])
					else:
						a = 1
				if a == 1:
					print('您查询的名字不存在!!')
			elif input_4 == 'c':
				a = 0
				tel_1 = input('请输入您查询的电话: ')
				data = db.resume.find({'tel':tel_1})
				for i in data:
					if i['tel'] == tel_1:
						print('编号: '+i['_id']+' 名字: '+i['name']+' 电话:'+i['tel']+' 经历:'+i['ex'])
					else:
						a = 1
				if a == 1:
					print('您查询的电话不存在!!')
			elif input_4 == 'd':
				a = 0
				ex_1 = input('请输入您查询的经历: ')
				data = db.resume.find({'ex':ex_1})
				for i in data:		
					if i['ex'] == ex_1:
						print('编号: '+i['_id']+' 名字: '+i['name']+' 电话:'+i['tel']+' 经历:'+i['ex'])
					else:
						a = 1
				if a == 1:
					print('您查询的经历不存在!!')
			elif input_4 == 'quit':
				print('已退出查找!!')
				break
			else:
				print('您选择的有误,请重新输入: ')
			
				
def main():
	resume=db_resume()
	while 1:
		print('''
		查看已经录入的简历信息:
		输入a,进行数据新增,
		输入b,进行数据删除,
		输入c,进行数据修改,
		输入d,进行数据查询,
		输入quit,退出.
		''')
		input_select=input('请输入您要选择的功能: ')
		if input_select == 'a':
			resume.resume_add()
		elif input_select == 'b':
			resume.resume_delete()
		elif input_select == 'c':
			resume.resume_update()
		elif input_select == 'd':
			resume.resume_find()
		elif input_select == 'quit':
			break
			print('您已退出系统!!')
		else:
			print('您选择的功能不存在,请重新选择: ')


if __name__ == '__main__':
	print('欢迎您登入简历系统!')
	main()





























































