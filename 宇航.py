import pymongo
b=pymongo.MongoClient(host='127.0.0.1',port=27017)
r=b.ku
def sys():
    while 1:
        a=input(
    '''欢迎来到简历管理系统，请输入命令:
------------------------------------
1.增加简历
2.删除简历
3.更改简历
4.查询简历
5.退出
------------------------------------
    '''
        )

        if a=='1':
            while 1:
                print('新增')
                n=input('请输入姓名:')
                t=int(input('请输入电话:'))
                e=input('请输入经历:')
                print('您刚才输入的是:\n\r\r\r\r姓名:%s 电话:%s 经历:%s  正确吗?'%(n,t,e))
                v=input('y/n:')
                if v=='y':
                    r.ku.insert({'ename':n,'tel':t,'exp1':e})
                    vv=input('写入成功，继续增加(1) ,返回上一层(2)')
                    if vv=='1':
                        continue
                    elif vv=='2':
                        break
                elif v=='n':
                    print('重新输入')
               
        elif a=='2':
            t=int(input('请输入要删除的简历的电话号码:'))
            r.ku.remove({'tel':t})
            print('已执行')
        elif a=='3':
            t1=int(input('请输入要改简历的号码:'))
            n=input('请输入新简历名字:')
            t2=int(input('请输入新简历的电话:'))
            e=input('请输入新的经历:')
            r.ku.update({'tel':t1},{'$set':{'ename':n,'tel':t2,'exp1':e }})
            print('已执行')
        elif a=='5':
            break
        elif a=='4':
            while 1:
                op=input(
    '''
--------------
请输入查询方式:
------------------------------------
1.按照电话进行查询 
2.按照名字进行查询
3.按照经历进行查询
4.显示所有简历
5.返回上一层
------------------------------------
    '''
        )
        
                if op=='1': 
                    t1=input('电话:')
                    rr=r.ku.find({'tel':t1})
                    for q in rr:
                        print('''名字:%s  电话:%s  经历:%s'''%(q['ename'],q['tel'],q['exp1']))
                elif op=='2':
                    n=input('姓名:')
                    rr=r.ku.find({'ename':n})
                    for q in rr:
                        print('''名字:%s  电话:%s  经历:%s'''%(q['ename'],q['tel'],q['exp1'])) 
                elif op=='3':
                    e=input('经历:')
                    rr=r.ku.find({'exp1':e})  
                    for q in rr:
                        print('''名字:%s  电话:%s  经历:%s'''%(q['ename'],q['tel'],q['exp1'])) 
                elif op=='4':
                    rr=r.ku.find()
                    for q in rr:
                        print('''名字:%s  电话:%s  经历:%s'''%(q['ename'],q['tel'],q['exp1'])) 
                        
                elif op=='5':
                    break
                else:
                    print('您的输入有误')
        else:
            print('您的输入有误')
sys()

    
