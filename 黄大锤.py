#coding=utf-8
import pymongo
conn=pymongo.MongoClient(host='127.0.0.1',port=27017)
db=conn.test
#输入
def add():
	name=input('请输入你的名字:')
	tel=input('请输入你的电话:')
	exp=input('请输入你的工作经历:')
	a=input('信息无误输入yes:')
	#添加
	if a=='yes':
		db.jianli.insert({'name':name,'tel':tel,'exp':exp})
		data=db.jianli.find()
		for i in data:
			print(i)
			print('简历数据新增成功')
#修改
def alt():
	a=[]	
	name1=input('请输入你需要查询的名字的信息:')
	chaxun=db.jianli.find({})
	a=[x for x in chaxun if name1==x['name']]
	if len(a)==0:
		print('简历表无此数据，无法进行修改')
	else:		
		print('可以修改')
		tel1=input('请修改电话:')
		exp1=input('请修改经历:')	
		xiugai=db.jianli.update({'name':name1},{'$set':{'tel':tel1,'exp':exp1}})
		print('修改成功')	
#删除
def de():
	name=input('请输入你需要删除的名字信息:')
	chaxun=db.jianli.find({})
	a=[x for x in chaxun if name==x['name']]
	if len(a)==0:
		print('简历表无此数据，无法进行删除')
	else:
		db.jianli.remove({'name':name})
		print('删除成功')
#查询
def find():
	name=input('请输入你需要删除的名字信息:')
	chaxun=db.jianli.find({})
	a=[x for x in chaxun if name==x['name']]
	if len(a)==0:
		print('没有该条数据，无法查询')
	else:           
		db.jianli.find({'name':name})
		print('修改成功')
def main():
#	通过a,b,c,d选择你需要的功能
#	a为新增，b为修改，c为删除，d为查询
	gongneng=input('请输入你需要使用的功能：')
	if gongneng=='a':
		print('进入新增功能')
		add()
	elif gongneng=='b':
		print('进入修改功能')
		alt()
	elif gongneng=='c':
		print('进入删除功能')
		de()
	elif gongneng=='d':
		find()
		print('进入查询功能')
	else:
		print('没有该功能')
main()
