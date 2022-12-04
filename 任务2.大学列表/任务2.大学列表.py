from pyecharts.charts import Bar
from pyecharts import options as opts
f1=open('大学数据源代码.txt','r',encoding='utf-8')
f2=open('univ.txt','w')
list_xy=[]
list_dx=[]
list_else=[]
for i in f1:
    if '学' in i:   #根据'学;进行第一波关键字提取
        c=i.split('alt=')[-1].split('"') #[-1]是指取列表最后一个元素
        #print(c)
        if len(c)>2 and '学院' in c[1]:  #根据学院和列表长度进行第二轮提取
            list_xy.append(c[1])  #把含有学院的高校加入列表
            f2.write(c[1]+'\n')
        if len(c)>2 and '大学' in c[1]:  #根据大学和列表长度进行第二轮提取
            list_dx.append(c[1]) #把含有大学的高校加入列表
            f2.write(c[1]+'\n')
    else:
        d=i.split('alt=')[-1].split('"') #根据指示进行其他组织的提取
        if d[0]=='' and len(d)==3:  #因为含有高校或者组织的列表切割完只有3个长度,所以这是一个标准
            #print(d)
            list_else.append(d[1]) #加入列表
f2.write('包含学院的名称数量为:{}\n包含大学的名称数量为:{}'.format(len(list_xy),len(list_dx)))     
f2.close()
#print(list_xy)
#print(list_dx)
#print(list_else)
dk={} #添加字典 
dk['学院']=len(list_xy) 
dk['大学']=len(list_dx)
dk['其他组织']=len(list_else)
print('学院数量为:{}\n大学数量为:{}\n其他组织数量为:{}'.format(len(list_xy),len(list_dx),len(list_else)))
x=list(dk.keys())#提取字典里的键做X轴
y=list(dk.values())##提取字典里的值作Y轴数据
bar1=Bar() #画图
bar1.add_xaxis(x)
bar1.add_yaxis('数据统计',y)
bar1.render('数量显示.html')
