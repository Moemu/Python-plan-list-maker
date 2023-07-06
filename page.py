def page1(sen,week,tit):
    txtdata = []
    txtdata.append('\n# '+tit+week)
    txtdata.append(sen)
    for i in range(15):
        count = 319 if i>=9 else 320
        txtdata.append(f'# **□** **{i+1}. {"_"*count}**')
    #每日小结（可自行选择删除）
    txtdata.append('# 小结')
    for i in range(5):
        txtdata.append(f'# **□** **{i+1}. {"_"*320}**')
    txtdata = '\n'.join(txtdata)
    return txtdata

def page2(sen,week,tit):
    txtdata = []
    txtdata.append('\n# '+tit+week)
    txtdata.append(sen)
    for i in range(10):
        count = 319 if i>=9 else 320
        txtdata.append(f'# **□** **{i+1}. {"_"*count}**')
    txtdata.append('# Weekend')
    for i in range(10):
        count = 319 if i>=9 else 320
        txtdata.append(f'# **□** **{i+1}. {"_"*count}**')
    txtdata = '\n'.join(txtdata)
    return txtdata