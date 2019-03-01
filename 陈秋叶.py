#coding=utf-8
import pymongo
#导入相应模块
conn=pymongo.MongoClient(host='127.0.0.1',port=27017)
#设置连接参数，IP地址，端口
#注意：127.0.0.1==localhost==电脑本机
db=conn.test

while 1:

	print('请输入要执行的操作：1为新增，2为查询，3为删除，4为修改，5为退出')
	print('---------------------------------------------------------------')
	z=input('******************** ')
	print('---------------------------------------------------------------')

#1.新增
	if z=='1':
		while 1:
			print('''
新增操作请按提示选择：
	输入1,新增信息
	输入2,退出新增程序
	''')
			choice1=input('请输入您的选择：')
			if choice1=='1':
				name1=input('请输入要新增的名字：')
				tel1=input('请输入要新增的号码：')
				ex1=input('请输入要新增的经历：')
			
				add1=input('''
			确认新增信息选择：yes
			返回上一步选择：no
			---------------------
			''')
				print('------------------')
				if add1=='yes':
					db.resumes.insert({'name':name1,'tel':tel1,'ex':ex1})
					data1=db.resumes.find()
					for i in data1:
						print('------------------')
						print('名字：'+i['name']+'\n电话: '+i['tel']+'\n经历：'+i['ex'])
						print('------------------')
						print(' 成功新增一条记录 ')
						print('------------------')
				elif add1=='no':
					print('已取消新增信息')
					continue
				else:
					print('-------------------------')
					print('输入有误，请选择yes或者no')
			elif choice1=='2':
				print('   已退出新增程序  ')
				print('-------------------')
				break
			else:
				print('---------------------------')
				print('您的输入有误，请选择1-2输入')

			
#2.查询
	elif z=='2':
		while 1:
			print('''
查询操作请按提示选择：
	输入1，按照名字进行查询
	输入2，按照电话进行查询
	输入3, 按照经历进行查询
	输入4, 查看表内所有数据
	输入5, 退出查询程序
	''')

			choice2=input('请输入您的选择: ')
			if choice2=='1':
				name2=input('请输入您查询的名字：')
				data2=db.resumes.find({'name':name2},{'_id':0})
				for i in data2:
					print('------------------')
					print('名字：'+i['name']+'\n电话: '+i['tel']+'\n经历：'+i['ex'])
					print('------------------')
			elif choice2=='2':
				tel2=input('请输入您查询的电话：')
				data2=db.resumes.find({'tel':tel2},{'_id':0})
				for i in data2:
					print('------------------')
					print('名字：'+i['name']+'\n电话: '+i['tel']+'\n经历：'+i['ex'])
					print('------------------')
			elif choice2=='3':
				ex2=input('请输入您查询的经历：')
				data2=db.resumes.find({'ex':ex2},{'_id':0})
				for i in data2:
					print('------------------')
					print('名字：'+i['name']+'\n电话: '+i['tel']+'\n经历：'+i['ex'])
					print('------------------')
			elif choice2=='4':
				data2=db.resumes.find()
				for i in data2:
					print('------------------')
					print('名字：'+i['name']+'\n电话: '+i['tel']+'\n经历：'+i['ex'])
					print('------------------')
			elif choice2=='5':
				print('-------------------')
				print('   已退出查询程序  ')
				print('-------------------')
				break
			else:
				print('---------------------------')
				print('您的输入有误！请选择1-5输入')
				print('---------------------------')




#3.删除
	elif z=='3':
		while 1:
			print('''
删除操作请按提示选择：
	删除指定名字的文档选择：1
	删除指定号码的文档选择：2
	删除指定经历的文档选择：3
	删除所有文档选择：4
	退出删除操作选择：5
		''')
			choice3=input('请输入您的选择：')
			if choice3=='1':
				name3=input('请输入要删除的名字：')
			
				db.resumes.remove({'name':name3})
				print('------------------')
				print('已成功删除一条文档')
				print('------------------')
			elif choice3=='2':
				tel3=input('请输入要删除的号码：')
				db.resumes.remove({'tel':tel3})
				print('------------------')
				print('已成功删除一条文档')
				print('------------------')
			elif choice3=='3':
				ex3=input('请输入要删除的经历：')
				db.resumes.remove({'ex':ex3})
				print('------------------')
				print('已成功删除一条文档')
				print('------------------')
			elif choice3=='4':
				del3=input('确认删除所有文档信息请选择yes,否则选择no:   ')
				if del3=='yes':
					db.resumes.remove()
					print('----------------------')
					print('已成功删除所有文档信息')
					print('----------------------')
				elif del3=='no':
					print('------------------')
					print('已取消删除所有文档')
				else:
					print('  输入错误  ')
					print('------------')

			elif choice3=='5':
				print('------------------')
				print('  已退出删除程序  ')
				print('------------------')
				break
			else:
				print('---------------------------')
				print('您的输入有误，请选择1-4输入')
			

				print('您的输入有误，请选择1-4输入')	
	elif z=='4':
		while 1:
			print('''
		修改操作请按提示选择：
			 根据指定名字修改请输入：1
			 根据指定号码修改请输入：2
			 根据指定经历修改请输入：3
			 退出修改程序请输入：4
			 
			 ''')
			update4=input('请输入您的选择：')
			if update4=='1':
				name4=input('请输入指定的名字：')
				db.resumes.find({'name':name4})
				data4=db.resumes.find({'name':name4})
				for i in data4:
					print('修改名字请按1,修改号码请按2,修改经历请按3,全部修改请按4,返回上一步请按5')
					print('-----------------------------------------------------------------------')
					xiugai=input('请输入您的选择：')
					if xiugai=='1':
						xiugai_name=input('请输入修改后的名字：')
						db.resumes.update({'name':name4},{'$set':{'name':xiugai_name}})
						data=db.resumes.find()
						for i in data:
							print('------------------')
							print('修改后信息为：''\n名字是  '+i['name']+'\n电话是  '+i['tel']+'\n经历是  '+i['ex'])
					elif xiugai=='2':
						xiugai_tel=input('请输入修改后的电话：')
						db.resumes.update({'name':name4},{'$set':{'tel':xiugai_tel}})
						data=db.resumes.find()
						for i in data:
							print('------------------')
							print('修改后信息为：''\n名字是  '+i['name']+'\n电话是  '+i['tel']+'\n经历是  '+i['ex'])
					elif xiugai=='3':
						xiugai_ex=input('请输入修改后的经历：')
						db.resumes.update({'name':name4},{'$set':{'ex':xiugai_ex}})
						data=db.resumes.find()
						for i in data:
							print('------------------')
							print('修改后信息为：''\n名字是  '+i['name']+'\n电话是  '+i['tel']+'\n经历是  '+i['ex'])
					elif xiugai=='4':
						xiugainame=input('请输入修改后的名字：')
						xiugaitel=input('请输入修改后的电话：')
						xiugaiex=input('请输入修改后的经历：')
						db.resumes.update({'name':name4},{'$set':{'name':xiugainame,'tel':xiugaitel,'ex':xiugaiex}})
						data=db.resumes.find()
						for i in data:
							print('------------------')
							print('修改后信息为：''\n名字是  '+i['name']+'\n电话是  '+i['tel']+'\n经历是  '+i['ex'])
					elif xiugai=='5':
						print('--------------')
						print('  返回上一步  ')
					else:
						print('------------')
						print('  输入错误  ')


			elif update4=='2':
				tel4=input('请输入指定的号码：')
				db.resumes.find({'tel':tel4})
				data4=db.resumes.find({'tel':tel4})
				for i in data4:
					print('修改名字请按1,修改号码请按2,修改经历请按3,全部修改请按4,返回上一步请按5')
					xiugai=input('请输入您的选择：')
					if xiugai=='1':
						xiugai_name=input('请输入修改后的名字：')
						db.resumes.update({'tel':tel4},{'$set':{'name':xiugai_name}})
						data=db.resumes.find()
						for i in data:
							print('------------------')
							print('修改后信息为：''\n名字是  '+i['name']+'\n电话是  '+i['tel']+'\n经历是  '+i['ex'])
					elif xiugai=='2':
						xiugai_tel=input('请输入修改后的电话：')
						db.resumes.update({'tel':tel4},{'$set':{'tel':xiugai_tel}})
						data=db.resumes.find()
						for i in data:
							print('------------------')
							print('修改后信息为：''\n名字是  '+i['name']+'\n电话是  '+i['tel']+'\n经历是  '+i['ex'])
					elif xiugai=='3':
						xiugai_ex=input('请输入修改后的经历：')
						db.resumes.update({'tel':tel4},{'$set':{'ex':xiugai_ex}})
						data=db.resumes.find()
						for i in data:
							print('------------------')
							print('修改后信息为：''\n名字是  '+i['name']+'\n电话是  '+i['tel']+'\n经历是  '+i['ex'])
					elif xiugai=='4':
						xiugainame=input('请输入修改后的名字：')
						xiugaitel=input('请输入修改后的电话：')
						xiugaiex=input('请输入修改后的经历：')
						db.resumes.update({'tel':tel4},{'$set':{'name':xiugainame,'tel':xiugaitel,'ex':xiugaiex}})
						data=db.resumes.find()
						for i in data:
							print('------------------')
							print('修改后信息为：''\n名字是  '+i['name']+'\n电话是  '+i['tel']+'\n经历是  '+i['ex'])
					elif xiugai=='5':
						print('返回上一步')
					else:
						print('输入错误')
			elif update4=='3':
				ex4=input('请输入指定的经历：')
				db.resumes.find({'ex':ex4})
				data4=db.resumes.find({'ex':ex4})
				for i in data4:
					print('修改名字请按1,修改号码请按2,修改经历请按3,全部修改请按4,返回上一步请按5')
					xiugai=input('请输入您的选择：')
					if xiugai=='1':
						xiugai_name=input('请输入修改后的名字：')
						db.resumes.update({'ex':ex4},{'$set':{'name':xiugai_name}})
						data=db.resumes.find()
						for i in data:
							print('------------------')
							print('修改后信息为：''\n名字是  '+i['name']+'\n电话是  '+i['tel']+'\n经历是  '+i['ex'])
					elif xiugai=='2':
						xiugai_tel=input('请输入修改后的电话：')
						db.resumes.update({'ex':ex4},{'$set':{'tel':xiugai_tel}})
						data=db.resumes.find()
						for i in data:
							print('------------------')
							print('修改后信息为：''\n名字是  '+i['name']+'\n电话是  '+i['tel']+'\n经历是  '+i['ex'])
					elif xiugai=='3':
						xiugai_ex=input('请输入修改后的经历：')
						db.resumes.update({'ex':ex4},{'$set':{'ex':xiugai_ex}})
						data=db.resumes.find()
						for i in data:
							print('------------------')
							print('修改后信息为：''\n名字是  '+i['name']+'\n电话是  '+i['tel']+'\n经历是  '+i['ex'])
					elif xiugai=='4':
						xiugainame=input('请输入修改后的名字：')
						xiugaitel=input('请输入修改后的电话：')
						xiugaiex=input('请输入修改后的经历：')
						db.resumes.update({'ex':ex4},{'$set':{'name':xiugainame,'tel':xiugaitel,'ex':xiugaiex}})
						data=db.resumes.find()
						for i in data:
							print('------------------')
							print('修改后信息为：''\n名字是  '+i['name']+'\n电话是  '+i['tel']+'\n经历是  '+i['ex'])
					elif xiugai=='5':
						print('返回上一步')
					else:
						print('输入错误')
			elif update4=='4':
				print('------------------')
				print('  已退出修改程序  ')
				print('------------------')
				break
			else:
				print('您的输入有误，请选择1-4输入')
				print('---------------------------')

#5.退出
	elif z=='5':
		print('已成功退出程序')
		break
#其他
	else:
		print('您的输入有误，请选择1-5输入')
		print('---------------------------------------------------------------')
