#coding=utf-8
import pymongo
conn=pymongo.MongoClient(host='127.0.0.1',port=27017)
db=conn.jianli
def chaxun(a):
	chaxun=db.jianli.find({'$or':[{'name':a},{'tel':a},{'exp':a}]})
	if chaxun.count()!=0:
		for i in chaxun:
			print('姓名: '+i['name']+',电话: '+i['tel']+',经历:'+i['exp'])
		return chaxun.count()
	else:
		print('无此信息!')
		return chaxun.count()

def dele(b):
	db.jianli.remove({'$or':[{'name':b},{'tel':b},{'exp':b}]})
	dele_chaxun=db.jianli.find({})
	for i in dele_chaxun:	
		print('姓名: '+i['name']+',电话: '+i['tel']+',经历:'+i['exp'])
	

while 1:
	a=input('输入您要办理的业务:1.新增简历 2.查看简历 3.删除简历 4.修改简历 5退出')
	if a=='1':
		while 1:
			name=input('姓名为:')
			tel=input('电话号码:')
			exp=input('经历为:')
			db.jianli.insert({'name':name,'tel':tel,'exp':exp})
			b=db.jianli.find({'name':name})
			for i in b:
				print('您增加:'+i['name']+'电话为:'+i['tel']+'经历为:'+i['exp'])
			jixu=input('退出请按q')
			if jixu=='q':
				break
			else:
				continue
	elif a=='2':
		while 1:
			cha=input('''
				a.通过姓名查询
				b.通过电话查询
				c.通过经历查询
				d.查询所有简历
				e.退出查询系统
				''')
			if cha=='a':
				name=input('输入名字:')
				chaxun(name)

			elif cha=='b':
				tel1=input('输入电话:')
				chaxun(tel1)
			elif cha=='c':
				exp1=input('输入经历:')
				chaxun(exp1)
			elif cha=='d':
				chaxun=db.jianli.find()
				for i in chaxun: 
					print('姓名: '+i['name']+',电话: '+i['tel']+',经历:'+i['exp'])
			elif cha=='e':
				break
			else:
				print('输入有误!')
	elif a=='3':
		while 1:
			del1=input('输入你要删除的姓名,或者电话,退出输入quit')
			if del1=='quit':
				break
			elif chaxun(del1)==0:
				print('请重新输入!')
				continue
			else: 
					#删除先查询,查询有的话再执行,若无,则告知
				del2=input('确认删除请输入y,退出d ')
				if del2=='y':
					dele(del1)		
				elif del2=='d':
					break
				else:
					print('输入有误')
	
	elif a=='4':
		while 1:
			modi=input('请输入您要修改的简历名称,退出请输入q ')
			if modi=='q':
				break
			else:	
				chaxun(modi)
				ch=input('输入您要修改的信息:a.电话,b.经历')
				if ch=='a':
					newtel=input('输入新的电话号码')
					db.jianli.update({'name':modi},{'$set':{'tel':newtel}})
				elif ch=='b':
					newexp=intput('输入新的经验:')
					db.jianli.update({'name':modi},{'$set':{'exp':newexp}})
				else:
					print('输入有误')
	elif a=='5':
		break

	else:
		print('输入有误!')
