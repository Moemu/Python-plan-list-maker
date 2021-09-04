#By WhitemuTeam
#Ver: 4.0(Pro)
#初始化
week=0 
import time,page,re
import PySimpleGUI as sg

#一言句子获取（随机分类）
def hitokoto():
    import requests as r
    try:
        web=r.get('https://v1.hitokoto.cn/?encode=text')
        web.encoding='utf-8'
        sen=web.text
        return sen
    except:
        sg.popup('请检查您的网络设置，如是否启用代理，如开启，请将其关闭')
        exit()

#自定义文本句子获取(sen.txt)
#取自issue #1(By AdminWhaleFall)

def txt():
    import random
    with open('sen.txt', 'r' , encoding='utf8') as f:
        datas = f.readlines()
        data  =  random.choice(datas)
    if data.strip() == '':
        txt()
    else:
        return data.strip() 

sg.theme('SystemDefaultForReal') #这是PysimpleGUI的主题之一，如果您不喜欢此主题，请参阅 https://blog.csdn.net/gainiu/article/details/113808314 查看其他主题

#GUI界面配置
layout=[[sg.Text('1*.请输入自定义标题，输入格式参阅readme.md(不填为Week)')],
        [sg.Input()],
        [sg.Text('2.请输入页数(必填)')],
        [sg.Input()],
        [sg.Text('3.请选择句子获取方式')],
        [sg.Radio('一言API', group_id=1),
        sg.Radio('自定义句子(sen.txt)', group_id=1)],
        [sg.Text('使用的模板：'),sg.Text('  '),sg.Text('是否检查引用的句子？')],
        [sg.InputCombo(['模板1','模板2'],size=(10,10)),sg.Text('  '),sg.Radio('是',group_id=2),sg.Radio('否',group_id=2)],
        [sg.Button('提交')]]

event,value=sg.Window('Plan list making(GUI)',icon='LOGO.ico').Layout(layout).Read() #启动GUI并获取值

#获取标题
tit=value[0]
if tit=='':
    tit='Week'

#获取制作数量
pages=int(value[1])
npages=int(value[1])

#读取句子获取方法
way=value[2]

#创建句子列表
def senlist(pages):
    senlists=''
    for i in range(pages):
        if way==True:
            sen=hitokoto()
            time.sleep(0.3)
        else:
            sen=txt()
        senlists=senlists+sen+' '
    senlists=senlists.split(' ')
    return senlists

senlists=senlist(pages)
del senlists[pages]

#检查句子
def check():
    sen='程序生成的句子如下'+'\n'
    a=0
    for i in senlists:
        sen=sen+'['+str(a)+']'+i+'\n'
        a=a+1
    sen=sen+'请确认您的句子是否合适，若不合适，请输入序号，用;号隔开，反之，则不输入'
    layout1=[[sg.Text(sen)],
        [sg.Input()],
        [sg.Button('确认')]]
    value=sg.Window('确认窗口',layout=layout1,icon='Logo.ico').Read()
    back=value[1][0]
    if back=='':
        pass
    else:
        backlist=back.split(';')
        show=''
        for i in backlist:
            i=int(i)
            oldsen=senlists[i]
            if way==True:
                nsen=hitokoto()
                senlists[i]=nsen
            else:
                nsen=txt()
                senlists[i]=nsen
            show=show+'更改完毕，源句子为：'+'\n'+oldsen+'\n'+'替换的句子为:'+'\n'+nsen+'\n'
        sg.popup(show,icon='LOGO.ico')
    return senlists
    
if value[5]==True:
    senlists=check()
    while True:
        layout2=[[sg.Text('还需要替换吗？')],
            [sg.Button('是',key='T'),sg.Button('否',key='F')]]
        event=sg.Window('是否继续替换？',layout=layout2,icon='LOGO.ico').Read()
        if event[0]=='T':
            senlists=check()
        else:
            break

#创建weekplan.md
doc=open('weekplan.md','w')
#导出
for i in senlists:
    sen=i
    week=week+1
    if value[4]=='模板1':
        try:
            pages=page.page1(sen,week,doc,tit,pages)
        except:
            sg.popup('未检测到page.py',icon='LOGO.ico')
    else:
        try:
            pages=page.page2(sen,week,doc,tit,pages)
        except:
            sg.popup('未检测到page.py',icon='LOGO.ico')
doc.close()   

sg.popup('导出完成，请打开weekplan.md查看',icon='LOGO.ico')
#end
