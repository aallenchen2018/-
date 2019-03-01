#coding=utf-8
import pymongo
conn=pymongo.MongoClient(host='127.0.0.1',port=27017)
db=conn.test

def find_pymo():
	ssname=input('请输入你要查询的东西:')
	message=input('请输入你想查询的内容:')
	data=db.xiyou.find({ssname:message})
	for i in data:
		print("名字"+i['name']+' '+"年龄"+str(i['age']+' '+'经验'+i['experience']))

def find_all():
	print('以下是库里面的所有信息')
	data=db.xiyou.find({},{'_id':0})
	for i in data:
		print("名字"+i['name']+' '+"年龄"+str(i['age']+' '+'经验'+i['experience']))

def add_pymo():
	nnname=input('请输入你新增的名字:')
	nnage=input('请输入你新增的年龄:')
	nnexp=input('请输入你新增的经验:')
	data=db.xiyou.insert({'name':nnname,'age':nnage,'experience':nnexp})

def modf_pymo():
	sstype=input('请输入你要输入的种类 (例如name/age/exp):')
	message=input('请输入你想选哪个:')
	info=input('请输入你要修改的:')
	con=input('请输入新的内容:')
	try:
		db.xiyou.update({sstype:message},{'$set':{info:con}})
	except:
		print('no exist!')
	finally:
		print('sucessfully!')

def delete_pymo():
	opt2=input('删除指定文档请按a，删除所有文档请按c:')
	if opt2 == 'a':
		del_doc=input('请输入指定文档的类型:')
		del_con=input('输入你想删的一个:')
		db.xiyou.remove({del_doc:del_con})
	elif opt2 == 'c':
		print('warnning!!')
		wa=input('pressing "go" to continue:')
		if wa == 'go':
			db.xiyou.remove()
		else:
			print('happy')

while True:
	cmmd=input('查询请按1,新增请按2,修改请按3,删除请按4,退出请按q:')
	if cmmd == '1':
		opt1=input('查询大概请按all，详细查询请按detial:')
		if opt1 == 'all':
			find_all()
		elif opt1 == 'detiak':
			find_pymo()
		print('OK lo')
	elif cmmd == '2':
		add_pymo()
		print('OK lo')
	elif cmmd == '3':
		modf_pymo()
	elif cmmd == '4':
		delete_pymo()
		print('OK lo')
	elif cmmd == 'q':
		print('see you tomorrow')
		break
	
