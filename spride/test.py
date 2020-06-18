novel_name = '我七岁就成了仙帝'
chapter_name = "test"
i = 1

f = open('d://novel//'+str(novel_name)+'//'+novel_name +
             str(i)+'.txt', 'a', encoding='utf-8')
f.write(chapter_name)