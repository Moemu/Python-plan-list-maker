# Plan list maker

# 2023.07.06更新

由于5.0及其以前的代码太过乐色，故我们重写了这个项目，新的主函数将存放在`main.py`，并且支持导出为PDF，但是，从2023.07.06开始，我们将停止对这个项目的维护并存档，如果有任何使用上的问题，请直接发邮件给我，感谢各位使用。

## 介绍

Plan list maker是基于Python的免费开源软件，其作用是制作一个精简的计划清单，如图所示：

![框架1](https://img.muspace.top/Page/planpaper.png)

该Planning list包含：

标题（Week or Day or more...） 例如：Week 1

名言警句 例如：能力越大，责任越大

支持20个计划：如果你的计划完成，那么你可以在对应的计划左边的框框处打勾（✔）

两个模板，一个带有总结、一个带有周末计划区域

## 使用：

在命令行安装第三方库：

```
pip install PySimpleGUI,markdown,pdfkit
```

运行`main.py`

按提示操作即可

## 句子

### 一言API

通过一言API获取句子，但其中的某些句子可能不够励志，您可以通过一言官网了解分类并更改`main.py`

### sen.txt

内置30个句子，来源于各大影视作品，整合来源：一言

如果想添加更多名言警句，可以更改`sen.txt`，直接新建一行输入您的句子即可（一句一行，注意长度不要太多）

## page.py

这是一个存放框架的Py文件，里面内置两个框架可供使用

![框架1](https://img.muspace.top/Page/planpaper.png)

![框架2](https://i.bmp.ovh/imgs/2021/09/af3a53a26e74ef22.png)

## 示例：

以下是我本人使用Planning list making制作的计划书：

![image-20210606104927589](https://img.muspace.top/Page/realplanpaper.jpg)

## 关于：

Planning list making Ver: 6.0

作者: Moemu

本作品遵守Apache 2.0协议，使用前请仔细阅读相关规则。