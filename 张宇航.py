import pymongo
b=pymongo.MongoClient(host='127.0.0.1',port=27017)
r=b.ku

a=int(input(
'''欢迎来到简历管理系统，请输入命令:
    ------------------------------------
    OC 1.增加简历
    OC 2.删除简历
    OC 3.更改简历
4.查询简历
5.退出
------------------------------------
'''
))
while 1:
if a==1:
n=input('请输入姓名:')
t=int(input('请输入电话:'))
e=input('请输入经历:')
r.ku.insert({'ename':n,'tel':t,'exp1':e})
elif a==2:
t=int(input('请输入要删除的简历的电话号码:'))
r.ku.remove({'tel':t})
elif a==3:
t1=int(input('请输入要改简历的号码:'))
n=input('请输入新简历名字:')
t2=int(input('请输入新简历的电话:'))
    e=input('请输入新的经历:')
    r.ku.update({'tel':t1},{'$set':{'ename':n,'tel':t2,'exp1':e }})
elif a==4:
    op=int(input(
'''
--------------
请输入查询方式:
------------------------------------
输入1,按照电话进行查询
输入2,按照名字进行查询
输入3,按照经历进行查询
输入4,显示所有简历
------------------------------------
'''
))

    if op==1: 
        t1=int(input('请输入电话:'))
        rr=r.ku.find({'tel':t1})
        for q in rr:
            print(q)
    elif op==2:
        n=input('ename')
        rr=r.ku.find({'请键输入姓名:':n})
        for q in rr:
            print(q)
    elif op==3:
        e=input('请输入经历:')
        rr=r.ku.find({'exp1':e})  
        for q in rr:
            print(q)
    elif op==4:
        rr=r.ku.find()
        for z in rr:
            print(z)
