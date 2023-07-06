from markdown import markdown
import time,page,random,pdfkit,os
import PySimpleGUI as sg

sg.set_options(font=('微软雅黑 10'))
sg.theme('Reddit')

def hitokoto():
    ''''
    获取一个一言在线句子
    '''
    import requests as r
    try:
        sen=r.get('https://v1.hitokoto.cn/?encode=text').text
        return sen
    except:
        sg.popup('请检查您的网络设置，如是否启用代理，如开启，请将其关闭')
        exit()

def CustomSen(filename:str):
    '''
    从文本文件中返回一个句子

    :filename *.txt
    '''
    with open(filename, 'r' , encoding='utf8') as f:
        datas = f.readlines()
        data = random.choice(datas)
    if data.strip() == '':
        CustomSen(filename)
    else:
        return data.strip() 

def GetSensList(pages:int,getmethod:str,filename:str=''):
    '''
    获取句子列表

    :pages 页数
    :getmethod 获取方法(0/1)
    :filename (可选)自定义句子集文件名 *.txt
    '''
    senslist = []
    for i in range(pages):
        if getmethod==True:
            sen=hitokoto()
            time.sleep(0.3)
        else:
            sen=CustomSen(filename)
        senslist.append(sen)
    return senslist

def CheckSens(senslist:list,getmethod:str,filename:str=''):
    '''
    检查获取到的句子是否合乎心水

    :pages 页数
    :getmethod 获取方法(0/1)
    :filename (可选)自定义句子集文件名 *.txt
    '''
    text='程序生成的句子如下'+'\n'
    for i,v in enumerate(senslist):
        text=text+'['+str(i)+']'+v+'\n'
    text=text+'请确认您的句子是否合适，若不合适，请输入序号，用;号隔开，反之，则不输入'

    layout1=[[sg.Text(text)],
        [sg.Input()],
        [sg.Button('确认')]]
    value=sg.Window('确认窗口',layout=layout1).Read()
    reselectsens=value[1][0]

    if reselectsens=='':
        pass
    else:
        reselectsenslist=reselectsens.split(';')
        show=''
        for i in reselectsenslist:
            i=int(i)
            oldsen=senslist[i]
            if getmethod==True:
                nsen=hitokoto()
                senslist[i]=nsen
            else:
                nsen=CustomSen(filename)
                senslist[i]=nsen
            show=show+'更改完毕，源句子为：'+'\n'+oldsen+'\n'+'替换的句子为:'+'\n'+nsen+'\n'
        sg.popup(show)

    return senslist

def OutputMarkdown(template:str,senslist:str,title:str):
    '''
    导出为Markdown文件

    :template 模板
    :senslist 句子列表
    :title 标题
    '''
    doc=open('weekplan.md','w',encoding='utf-8')
    week = 0
    for i in senslist:
        sen=i
        week+=1
        w = str(week)
        if template=='模板1':
            txtdata = page.page1(sen,w,title)
        else:
            txtdata = page.page2(sen,w,title)
        doc.write(txtdata)
    doc.close()

def OutputPDF():
    '''
    将Markdown文件转换为PDF文件

    :filename Markdown文件路径
    '''
    input_filename = 'weekplan.md'
    output_filename = 'weekplan.pdf'
    with open(input_filename, encoding='utf-8') as f:
        text = f.read()
    html = markdown(text, output_format='html')  # MarkDown转HTML
    wkhtmltopdf = r'wkhtmltox\bin\wkhtmltopdf.exe'  # 指定wkhtmltopdf
    configuration = pdfkit.configuration(wkhtmltopdf=wkhtmltopdf)
    pdfkit.from_string(html, output_filename, configuration=configuration, options={'encoding': 'utf-8'})  # HTML转PDF

def wkhtmltox_check() -> None:
    '''
    检查是否存在 wkhtmltox
    '''
    try:
        os.chdir('wkhtmltox')
        os.chdir('..')
        return True
    except:
        layout=[
            [sg.Text('该功能需要第三方应用程序: wkhtmltox 的支持',font=('微软雅黑 10'))],
            [sg.Text('请问要现在下载吗? ( 46M 预计1分钟以内 )',font=('微软雅黑 10'))],
            [sg.Button('是',font=('微软雅黑 10')),sg.Button('否',font=('微软雅黑 10'))]
        ]
        windows=sg.Window('第三方软件下载提示',layout=layout)
        event,value=windows.Read()
        if event==sg.WIN_CLOSED:
            windows.Close()
            return False
        if event=='是':
            windows=sg.Window('下载中',layout=[[sg.Text('下载中, 这通常需要一点时间...',font=('微软雅黑 10'))]])
            windows.read(timeout=100)
            import requests as r
            import zipfile
            try:
                url='https://file.muspace.top/Program/wkhtmltox.zip'
                file=r.get(url)
                open('wkhtmltox.zip','wb').write(file.content)
                with zipfile.ZipFile('wkhtmltox.zip') as zf:
                    zf.extractall()
                os.remove('wkhtmltox.zip')
                windows.Close()
            except:
                sg.Popup('wkhtmltox 下载失败, 请检查是否已联网或者是已关闭代理',font=('微软雅黑 10'))
            return True
        else:
            windows.Close()
            return False

def main():
    layout=[[sg.Text('1*.请输入任务书标题')],
            [sg.Input()],
            [sg.Text('2.请输入页数(必填)')],
            [sg.Input()],
            [sg.Text('3.请选择句子获取方式')],
            [sg.Radio('一言API', group_id=1),sg.Radio('自定义句子集', group_id=1)],
            [sg.Text('4*.若使用自定义句子集,请输入句子集文本文件路径')],
            [sg.Input(),sg.FileBrowse(button_text='浏览',file_types=(('文本文件','*.txt'),))],
            [sg.Text('5.请选择导出文件格式')],
            [sg.InputCombo(['Markdown','PDF'],default_value='PDF')],
            [sg.Text('使用的模板：'),sg.Text('  '),sg.Text('是否检查引用的句子？')],
            [sg.InputCombo(['模板1','模板2'],default_value='模板2',size=(10,10)),sg.Text('  '),sg.Radio('是',group_id=2),sg.Radio('否',group_id=2)],
            [sg.Button('提交')]]
    while True:
        event,value=sg.Window('Plan list making(GUI)').Layout(layout).Read()
        if event==sg.WIN_CLOSED:
            break

        title=value[0] if value[0] != '' else 'Week'
        pages=int(value[1])
        getmethod=value[2]
        filename=value[4]
        outputformat=value[5]
        template=value[6]
        checksens=value[7]

        senslist = GetSensList(pages,getmethod,filename)

        if checksens==True:
            senslist=CheckSens(senslist,getmethod,filename)
            while True:
                layout2=[[sg.Text('还需要替换吗？')],
                    [sg.Button('是',key='T'),sg.Button('否',key='F')]]
                event=sg.Window('是否继续替换？',layout=layout2).Read()
                if event[0]=='T':
                    senslist=CheckSens(senslist,getmethod,filename)
                else:
                    break

        OutputMarkdown(template,senslist,title)
        if outputformat == 'PDF':
            wkhtmltox_check()
            OutputPDF()

        sg.popup('导出完成，请打开weekplan.md或weekplan.pdf查看')
        return None

if __name__ == '__main__':
    main()