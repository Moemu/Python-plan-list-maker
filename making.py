week=0 #初始化
from sen import sen #导入sen（外部句子）函数
#介绍
print('欢迎使用Plan list making！') 
print('当前版本V1.0(beta)')
print('作者:White_mu Github:@WhitemuTeam')
#开始
t=int(input('请输入需要制作的计划清单数量：'))
print('--------------------------------------------------------------------------分割线---------------------------------------------------------------')
#导出
while (t > 0):
    week=week+1
    sens=sen() #从sen中获取句子
    print('# Week ',week) #标题（默认为Week，可更改为Day，例如:'#Day ',week）
    print(sens) #引用句子
    print('# **□** **1. _______________________________________________________________________________________________________________________________**')
    print('# **□** **2. _______________________________________________________________________________________________________________________________**')
    print('# **□** **3. _______________________________________________________________________________________________________________________________**')
    print('# **□** **4. _______________________________________________________________________________________________________________________________**')
    print('# **□** **5. _______________________________________________________________________________________________________________________________**')
    print('# **□** **6. _______________________________________________________________________________________________________________________________**')
    print('# **□** **7. _______________________________________________________________________________________________________________________________**')
    print('# **□** **8. _______________________________________________________________________________________________________________________________**')
    print('# **□** **9. _______________________________________________________________________________________________________________________________**')
    print('# **□** **10. ______________________________________________________________________________________________________________________________**')
    print('# **□** **11. ______________________________________________________________________________________________________________________________**')
    print('# **□** **12. ______________________________________________________________________________________________________________________________**')
    print('# **□** **13. ______________________________________________________________________________________________________________________________**')
    print('# **□** **14. ______________________________________________________________________________________________________________________________**')
    print('# **□** **15. ______________________________________________________________________________________________________________________________**')
    #每日小结（可自行选择删除）
    print('# 本周小结：')
    print('# **________________________________________________________________________________________________________________________________________________**')
    print('# **________________________________________________________________________________________________________________________________________________**')
    print('# **________________________________________________________________________________________________________________________________________________**')
    t=t-1
print('--------------------------------------------------------------------------分割线---------------------------------------------------------------')
print('导出完成，请用Markdown编辑器并开始源代码模式复制分割线的内容即可')
input('按任意键关闭此程序')
#end