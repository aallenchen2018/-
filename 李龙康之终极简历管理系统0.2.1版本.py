import pymongo
conn=pymongo.MongoClient(host='127.0.0.1',port=27017)
db=conn.resume
while 1:
	print('''
输入1，新增模式
输入2，修改模式
输入3，删除模式
输入4，查看模式
输入q，退出程序
	''')
	xuan=input('请选择模式:')
	if xuan=='1':
		while 1:
			print('欢迎进入新增模式')
			name=input('请输入您的姓名:')
			age=input('请输入您的年龄:')
			tel=input('请输入您的电话:')
			su=input('确定信息无误吗?(确定yes,取消no,退出q):')
			if su=='yes':
				db.resumes.insert({'name':name,'age':age,'phone':tel})
				print('添加成功')
				print('新增后数据表为:')
				data=db.resumes.find()
				for i in data:
					print('名字:'+i['name'],'、'+'年龄:'+i['age'],'、'+'电话:'+i['phone'])
				shu=input('是否继续执行新增模块(继续yes,退出q):')
				if shu=='yes':
					print('新增模块继续运行')
				elif shu=='q':
					print('已退出')
					break
				else:
					print('请输入yes或q,输入错误继续运行')
			elif su=='no':
				print('请重新输入信息')
			elif su=='q':
				print('已退出')
				break
			else:
				print('请重新输入信息')
	elif xuan=='2':
		while 1:
			print('欢迎进入修改模式')
			print('''
			修改已经录入的简历信息
			输入a，按照名字进行修改
			输入b，按照年龄进行修改
			输入c, 按照电话进行修改
			输入q, 退出程序
			''')
			shuru=input('请输入您的选择:')
			if shuru=='a':
				name=input('请输入要修改的名字:')
				data=db.resumes.find({'name':name},{'_id':0})
				a = [j for j in data if name == j['name']]
				if len(a) == 0:
					print('名字不存在哦!')
					jixu=input('退出按q,其他键继续:')
					if jixu=='q':
						print('退出成功!')
						break
				else:	
					while 1:
						data=db.resumes.find({'name':name},{'_id':0})
						for i in data:
							print('您要修改的原数据为:','名字:'+i['name'],'、'+'年龄:'+i['age'],'、'+'电话:'+i['phone'])
						print('''
			修改已经录入的简历信息
			输入1, 修改名字
			输入2，修改年龄
			输入3, 修改电话
			输入4, 修改所有
			输入q，返回上一步
							''')
						shuru1=input('请再次输入您的选择:')
						if shuru1=='1':
							name1=input('请输入修改后的名字:')
							que=input('请确认(yes或no):')
							if que=='no':
								print('请重新输入')
							elif que=='yes':
								db.resumes.update({'name':name},{'$set':{'name':name1}})
								data=db.resumes.find({'name':name1})
								for i in data:
									print('您修改后数据为:','名字:'+i['name'],'、'+'年龄:'+i['age'],'、'+'电话:'+i['phone'])
									print('--------------下一次---------------')
							else:
								print('输入错误，默认取消，请重新输入')
						elif shuru1=='2':
							age1=input('请输入修改后的年龄:')
							que=input('请确认(yes或no):')
							if que=='no':
								print('请重新输入')
							elif que=='yes':
								db.resumes.update({'name':name},{'$set':{'age':age1}})
								data=db.resumes.find({'age':age1})
								for i in data:
									print('您修改后数据为:','名字:'+i['name'],'、'+'年龄:'+i['age'],'、'+'电话:'+i['phone'])
									print('--------------下一次---------------')
							else:
								print('输入错误，默认取消，请重新输入')
						elif shuru1=='3':
							tel1=input('请输入修改后的电话:')
							que=input('请确认(yes或no):')
							if que=='no':
								print('请重新输入')
							elif que=='yes':
								db.resumes.update({'name':name},{'$set':{'phone':tel1}})
								data=db.resumes.find({'phone':tel1})
								for i in data:
									print('您修改后数据为:','名字:'+i['name'],'、'+'年龄:'+i['age'],'、'+'电话:'+i['phone'])
									print('--------------下一次---------------')
							else:
								print('输入错误，默认取消，请重新输入')
						elif shuru1=='4':
							name1=input('请输入修改后的名字:')
							age1=input('请输入修改后的年龄:')
							tel1=input('请输入修改后的电话:')
							que=input('请确认(yes或no):')
							if que=='no':
								print('请重新输入')
							elif que=='yes':
								db.resumes.update({'name':name},{'$set':{'name':name1,'age':age1,'phone':tel1}})
								data=db.resumes.find({'name':name1})
								for i in data:
									print('您修改后数据为:','名字:'+i['name'],'、'+'年龄:'+i['age'],'、'+'电话:'+i['phone'])
									print('--------------下一次---------------')
							else:
								print('输入错误，默认取消，请重新输入')
						elif shuru1=='q':
							print('正在返回上一步')
							break
						else:
							print('输入错误，请重新输入')

			elif shuru=='b':
				age=input('请输入要修改的年龄:')
				data=db.resumes.find({'age':age},{'_id':0})	
				a = [j for j in data if age == j['age']]
				if len(a) == 0:
					print('年龄不存在哦!')
					jixu=input('退出按q,其他键继续:')
					if jixu=='q':
						print('退出成功!')
						break
				else:	
					while 1:
						data=db.resumes.find({'age':age},{'_id':0})	
						for i in data:
							print('您要修改的原数据为:','名字:'+i['name'],'、'+'年龄:'+i['age'],'、'+'电话:'+i['phone'])
						print('''
			修改已经录入的简历信息
			输入1, 修改名字
			输入2，修改年龄
			输入3, 修改电话
			输入4, 修改所有
			输入q，返回上一步
							''')
						shuru1=input('请再次输入您的选择:')
						if shuru1=='1':
							name1=input('请输入修改后的名字:')
							que=input('请确认(yes或no):')
							if que=='no':
								print('请重新输入')
							elif que=='yes':
								db.resumes.update({'age':age},{'$set':{'name':name1}})
								data=db.resumes.find({'name':name1})
								for i in data:
									print('您修改后数据为:','名字:'+i['name'],'、'+'年龄:'+i['age'],'、'+'电话:'+i['phone'])
									print('--------------下一次---------------')
							else:
								print('输入错误，默认取消，请重新输入')
						elif shuru1=='2':
							age1=input('请输入修改后的年龄:')
							que=input('请确认(yes或no):')
							if que=='no':
								print('请重新输入')
							elif que=='yes':
								db.resumes.update({'age':age},{'$set':{'age':age1}})
								data=db.resumes.find({'age':age1})
								for i in data:
									print('您修改后数据为:','名字:'+i['name'],'、'+'年龄:'+i['age'],'、'+'电话:'+i['phone'])
									print('--------------下一次---------------')
							else:
								print('输入错误，默认取消，请重新输入')
						elif shuru1=='3':
							tel1=input('请输入修改后的电话:')
							que=input('请确认(yes或no):')
							if que=='no':
								print('请重新输入')
							elif que=='yes':
								db.resumes.update({'age':age},{'$set':{'phone':tel1}})
								data=db.resumes.find({'phone':tel1})
								for i in data:
									print('您修改后数据为:','名字:'+i['name'],'、'+'年龄:'+i['age'],'、'+'电话:'+i['phone'])
									print('--------------下一次---------------')
							else:
								print('输入错误，默认取消，请重新输入')
						elif shuru1=='4':
							name1=input('请输入修改后的名字:')
							age1=input('请输入修改后的年龄:')
							tel1=input('请输入修改后的电话:')
							que=input('请确认(yes或no):')
							if que=='no':
								print('请重新输入')
							elif que=='yes':
								db.resumes.update({'age':age},{'$set':{'name':name1,'age':age1,'phone':tel1}})
								data=db.resumes.find({'name':name1})
								for i in data:
									print('您修改后数据为:','名字:'+i['name'],'、'+'年龄:'+i['age'],'、'+'电话:'+i['phone'])
									print('--------------下一次---------------')
							else:
								print('输入错误，默认取消，请重新输入')
						elif shuru1=='q':
							print('正在返回上一步')
							break
						else:
							print('输入错误，请重新输入')

			elif shuru=='c':
				tel=input('请输入要修改的电话:')
				data=db.resumes.find({'phone':tel},{'_id':0})
				a = [j for j in data if tel == j['phone']]
				if len(a) == 0:
					print('电话不存在哦!')
					jixu=input('退出按q,其他键继续:')
					if jixu=='q':
						print('退出成功!')
						break
				else:	
					while 1:
						data=db.resumes.find({'phone':tel},{'_id':0})
						for i in data:
							print('您要修改的原数据为:','名字:'+i['name'],'、'+'年龄:'+i['age'],'、'+'电话:'+i['phone'])
						print('''
				修改已经录入的简历信息
				输入1, 修改名字
				输入2，修改年龄
				输入3, 修改电话
				输入4, 修改所有
				输入q，返回上一步
							''')
						shuru1=input('请再次输入您的选择:')
						if shuru1=='1':
							name1=input('请输入修改后的名字:')
							que=input('请确认(yes或no:)')
							if que=='no':
								print('请重新输入')
							elif que=='yes':
								db.resumes.update({'phone':tel},{'$set':{'name':name1}})
								data=db.resumes.find({'name':name1})
								for i in data:
									print('您修改后数据为:','名字:'+i['name'],'、'+'年龄:'+i['age'],'、'+'电话:'+i['phone'])
									print('--------------下一次---------------')
							else:
								print('输入错误，默认取消，请重新输入')
						elif shuru1=='2':
							age1=input('请输入修改后的年龄:')
							que=input('请确认(yes或no:)')
							if que=='no':
								print('请重新输入')
							elif que=='yes':
								db.resumes.update({'phone':tel},{'$set':{'age':age1}})
								data=db.resumes.find({'age':age1})
								for i in data:
									print('您修改后数据为:','名字:'+i['name'],'、'+'年龄:'+i['age'],'、'+'电话:'+i['phone'])
									print('--------------下一次---------------')
							else:
								print('输入错误，默认取消，请重新输入')
						elif shuru1=='3':
							tel1=input('请输入修改后的电话:')
							que=input('请确认(yes或no:)')
							if que=='no':
								print('请重新输入')
							elif que=='yes':
								db.resumes.update({'phone':tel},{'$set':{'phone':tel1}})
								data=db.resumes.find({'phone':tel1})
								for i in data:
									print('您修改后数据为:','名字:'+i['name'],'、'+'年龄:'+i['age'],'、'+'电话:'+i['phone'])
									print('--------------下一次---------------')
							else:
								print('输入错误，默认取消，请重新输入')
						elif shuru1=='4':
							name1=input('请输入修改后的名字:')
							age1=input('请输入修改后的年龄:')
							tel1=input('请输入修改后的电话:')
							que=input('请确认(yes或no:)')
							if que=='no':
								print('请重新输入')
							elif que=='yes':
								db.resumes.update({'phone':tel},{'$set':{'name':name1,'age':age1,'phone':tel1}})
								data=db.resumes.find({'name':name1})
								for i in data:
									print('您修改后数据为:','名字:'+i['name'],'、'+'年龄:'+i['age'],'、'+'电话:'+i['phone'])
									print('--------------下一次---------------')
							else:
								print('输入错误，默认取消，请重新输入')
						elif shuru1=='q':
							print('正在返回上一步')
							break
						else:
							print('输入错误，请重新输入')
			elif shuru=='q':
				print('退出成功')
				break
			else:
				print('输入错误，请重新输入')
	elif xuan=='3':
		while 1:
			print('欢迎进入删除模式')
			print('''
			修改已经录入的简历信息
			输入a，按照名字进行删除
			输入b，按照年龄进行删除
			输入c, 按照电话进行删除
			输入d, 删除数据库中所有数据
			输入q, 退出程序
			''')
			shuru=input('请输入您的选择:')
			if shuru=='a':
				name=input('请输入要删除的名字:')
				data=db.resumes.find({'name':name},{'_id':0})
				a = [j for j in data if name == j['name']]
				if len(a) == 0:
					print('名字不存在')
					jixu=input('退出按q,其他键继续哦:')
					if jixu=='q':
						print('退出成功!')
						break
				else:
					data=db.resumes.find({'name':name},{'_id':0})
					for i in data:
						print('您要删除的数据为:','名字:'+i['name'],'、'+'年龄:'+i['age'],'、'+'电话:'+i['phone'])
					que=input('请确认(yes或no):')
					if que=='no':
						print('请重新输入')
					elif que=='yes':
						db.resumes.remove({'name':name})
						print('删除成功')
					else:
						print('输入错误，默认取消，请重新输入')
			elif shuru=='b':
				age=input('请输入要删除的年龄:')
				data=db.resumes.find({'age':age},{'_id':0})
				a = [j for j in data if age == j['age']]
				if len(a) == 0:
					print('年龄不存在')
					jixu=input('退出按q,其他键继续哦:')
					if jixu=='q':
						print('退出成功!')
						break
				else:
					data=db.resumes.find({'age':age},{'_id':0})
					for i in data:
						print('您要删除的数据为:','名字:'+i['name'],'、'+'年龄:'+i['age'],'、'+'电话:'+i['phone'])
					que=input('请确认(yes或no):')
					if que=='no':
						print('请重新输入')
					elif que=='yes':
						db.resumes.remove({'age':age})
						print('删除成功')
					else:
						print('输入错误，默认取消，请重新输入')
			elif shuru=='c':
				tel=input('请输入要删除的电话:')
				data=db.resumes.find({'phone':tel},{'_id':0})
				a = [j for j in data if tel == j['phone']]
				if len(a) == 0:
					print('电话不存在')
					jixu=input('退出按q,其他键继续哦:')
					if jixu=='q':
						print('退出成功!')
						break
				else	:
					data=db.resumes.find({'phone':tel},{'_id':0})
					for i in data:
						print('您要删除的数据为:','名字:'+i['name'],'、'+'年龄:'+i['age'],'、'+'电话:'+i['phone'])
					que=input('请确认(yes或no):')
					if que=='no':
						print('请重新输入')
					elif que=='yes':
						db.resumes.remove({'phone':tel})
						print('删除成功')
					else:
						print('输入错误，默认取消，请重新输入')
			elif shuru=='d':
				data=db.resumes.find()
				print('您要删除的全部数据为:')
				for i in data:
					print('名字:'+i['name'],'、'+'年龄:'+i['age'],'、'+'电话:'+i['phone'])
				que=input('请确认(yes或no):')
				if que=='no':
					print('请重新输入')
				elif que=='yes':
					que1=input('真的确认吗!删除所有数据(yes或no):')
					if que1=='no':
						print('请重新输入')
					elif que1=='yes':
						db.resumes.remove()
						print('删除成功')
					else:
						print('输入错误，默认取消，请重新输入')
				else:
					print('输入错误，默认取消，请重新输入')
			elif shuru=='q':
				print('退出成功!')
				break
			else:
				print('输入错误，请重新输入')

	elif xuan=='4':
		while 1:
			print('欢迎进入查询模式')
			print('''
			查看已经录入的简历信息
			输入a，按照名字进行查询
			输入b，按照年龄进行查询
			输入c, 按照电话进行查询
			输入d, 查询所有数据
			输入q, 退出程序
			''')
			shuru=input('请输入您的选择: ')
			if shuru=='a':
				name=input('请输入您查询的名字:')
				data=db.resumes.find({'name':name},{'_id':0})
				a = [j for j in data if name == j['name']]
				if len(a) == 0:
					print('名字不存在哦!')
					jixu=input('退出按q,其他键继续:')
					if jixu=='q':
						print('退出成功!')
						break
				else:
					data=db.resumes.find({'name':name},{'_id':0})
					for i in data:
						print('您要查询的数据为:','名字:'+i['name'],'、'+'年龄:'+i['age'],'、'+'电话:'+i['phone'])
					print('--------------下一次---------------')
			elif shuru=='b':
				age=input('请输入您查询的年龄:')
				data=db.resumes.find({'age':age},{'_id':0})
				a = [j for j in data if name == j['name']]
				if len(a) == 0:
					print('年龄不存在哦!')
					jixu=input('退出按q,其他键继续:')
					if jixu=='q':
						print('退出成功!')
						break
				else:	
					data=db.resumes.find({'name':name},{'_id':0})
					for i in data:
						print('您要查询的数据为:','名字:'+i['name'],'、'+'年龄:'+i['age'],'、'+'电话:'+i['phone'])
					print('--------------下一次---------------')
			elif shuru=='c':
				tel=input('请输入您查询的电话:')
				data=db.resumes.find({'phone':tel},{'_id':0})
				a = [j for j in data if name == j['name']]
				if len(a) == 0:
					print('电话不存在哦!')
					jixu=input('退出按q,其他键继续:')
					if jixu=='q':
						print('退出成功!')
						break
				else:	
					data=db.resumes.find({'name':name},{'_id':0})
					for i in data:
						print('您要查询的数据为:','名字:'+i['name'],'、'+'年龄:'+i['age'],'、'+'电话:'+i['phone'])
					print('--------------下一次---------------')
			elif shuru=='d':
					data=db.resumes.find()
					for i in data:
						print('所有数据为:')
						print('名字:'+i['name'],'、'+'年龄:'+i['age'],'、'+'电话:'+i['phone'])
					print('--------------下一次---------------')
			elif shuru=='q':
				print('已退出')
				break
			else:
				print('您输入有误!!!')
	elif xuan=='q':
		print('退出成功!')
		break
	else:
		print('请重新输入')



















