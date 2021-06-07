#sen函数
#请注意：该句子的来源于一言，项目地址：https://github.com/hitokoto-osc/sentences-bundle/blob/master/sentences
#引用请表明出处
#导入句子教程
#在def下添加：
#if num==a: （a为当前句子数+1）
#    sen='你的句子'
#例如：
#def sen():
#    num=int(random.randint(1,12) ) #12=11+1
#    ......（此处省略）
#    if num==12:
#         sen='能力越大，责任越大'
def sen():
	import random
	num=int(random.randint(1,11)) #依据句子数量更改，当句子数量为20时，则更改为（1,20）
	if num==1:
		sen='没有了对高处的恐惧，就体会不到高处之美'
	if num==2:
		sen='终此一生，只有两种办法：要么梦见生活，要么落实生活。'
	if num==3:
		sen='永远相信美好的事情即将发生'
	if num==4:
		sen='唯有信仰与日月亘古不灭。'
	if num==5:
		sen='我们嘲笑过少年的无知，也嘲笑过岁月的苍老。我们行走在路上，理想宏大，眼窝却浅显。'
	if num==6:
		sen='既然选择了远方，便只顾风雨兼程。'
	if num==7:
		sen='哪有什么岁月静好，只是有人在替你负重前行。'
	if num==8:
		sen='没有谁的生活会一直完美，但无论什么时候，都要看着前方，满怀希望就会所向披靡。'
	if num==9:
		sen='两千三百一十二天，他们相遇在寒风朔雪中。以为是初见，其实是重逢'
	if num==10:
		sen='愿你出走半生，归来仍是少年。'
	if num==11:
		sen='世界灿烂盛大，欢迎回家。'
	return sen