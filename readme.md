# Plan list maker

注意：我们将在5.0版本移除making.py，源makingpro.py将代替making.py

## 介绍

Plan list maker是基于Python的免费开源软件，其作用是制作一个精简的计划清单，如图所示：

![框架1](https://cdn.jsdelivr.net/gh/WhitemuTeam/web-img/planpaper.png)

该Planning list包含：

标题（Week or Day or more...） 例如：Week 1

名言警句 例如：能力越大，责任越大

支持15个计划（最高19个）：如果你的计划完成，那么你可以在对应的计划左边的框框处打勾（✔）

*每日（周）总结（可选，默认开启） ：支持写3行的总结，总结你最近做了什么，还要改进的地方在哪里

当然你也可以选择关闭，只需删除对应的代码即可.

## 使用：

### 普通版

适用于电脑配置低的用户（仅支持制作页数更改）

运行`making.py` 或者是`making.exe` 

输入需要制作Planning list的页数（1代表1周或1天）

等待输出

输出结果如下：

```Python
欢迎使用Plan list making！
当前版本V3.0
作者:White_mu Github:@WhitemuTeam
请输入需要制作的计划清单数量：3
导出完成，请打开weekplan.md查看
按任意键关闭此程序
```

用Markdown编辑器打开weekplan.md（例如：Typora，玩Github的应该人手一个Markdown编辑器吧）并打开源代码模式，粘贴刚才复制的内容，在顶部菜单栏依次点击文件>打印，打印即可（建议先用Microsoft Print to PDF预览一下，以免出现不必要的麻烦）

注意：近日有用户反馈打印时出现横线过长的情况，现提供以下解决方案：

1.使用Typora导出或打印

2.更改源代码并调整横线长度

### 高级版

适用于电脑配置一般，且有自定义需求的用户（GUI界面，支持标题更改，句子来源选择，页数选择）

注意：您需要安装下列库，否则您可能无法运行`makingpro.py`（makingpro.exe除外）：
在命令行输入：

```
pip install PySimpleGUI
pip install requests
```

运行`makingpro.py`或`makingpro.exe`，按指示输入设置项

随后的操作和普通版类似

## 修改：

计划清单的标题可修改，默认是Week

1.你可以在making.py修改（适用于普通版），修改以下内容：

```python
print('# Week ',week,file=doc) #标题（默认为Week，可更改为Day，例如:'#Day ',week）
```

修改# week即可，例：

```python
print('# Day ',week,file=doc) #标题（默认为Week，可更改为Day，例如:'#Day ',week）
```

2.你可以通过`makingpro.py`或`makingpro.exe`修改：

打开`makingpro.py`或``makingpro.exe`：

它会提示您修改标题，输入你想要修改的标题（例: Day 默认:Week）即可。

注意：无论是输入什么，后面总会显示数量，要移除请自行修改`makingpro.py`

## 句子

### 一言API

（仅适用于`makingpro.py`或`makingpro.exe`）

通过一言API获取句子，但其中的某些句子可能不够励志，您可以通过一言官网了解分类并更改`makingpro.py`

### sen.txt

内置30个句子，来源于各大影视作品，整合来源：一言

如果想添加更多名言警句，可以更改`sen.txt`，直接新建一行输入您的句子即可（一句一行，注意长度不要太多）

## page.py

这是一个存放框架的Py文件，里面内置两个框架可供使用（仅供Pro版）

![框架1](https://cdn.jsdelivr.net/gh/WhitemuTeam/web-img/planpaper.png)

![框架2](https://i.bmp.ovh/imgs/2021/09/af3a53a26e74ef22.png)

## 示例：

以下是我本人使用Planning list making制作的计划书：

![image-20210606104927589](https://cdn.jsdelivr.net/gh/WhitemuTeam/web-img/realplanpaper.jpg)

## 关于：

Planning list making Ver: 5.0

作者:White_mu

本作品遵守Apache 2.0协议，未经许可严禁转载