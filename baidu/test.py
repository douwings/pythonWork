#coding=utf-8
from aip import AipSpeech
import re

APP_ID = "16051129"
API_KEY = "qdlO92S6g0DIkCT3CEB3S1uv"
SECRET_KEY = "KDvHo9UWXlCZcur4EiHHNzt5h4C0HgIK"

client = AipSpeech(APP_ID,API_KEY,SECRET_KEY)

text = ''''''
def cut_text(text,lenth):
    textArr = re.findall('.{'+str(lenth)+'}', text)
    textArr.append(text[(len(textArr)*lenth):])
    return textArr


textarr = cut_text(text,450)

res = []

for i in range(len(textarr)):
    res.append(client.synthesis(textarr[i],"zh",1,{
        'vol':5,
        'spd':4,
        'pit':8,
        'per':4,
    }))


# print(res)

# res2 = client.synthesis("一顿操作猛如虎，一看战绩零杠五","zh",1,{
#     'vol':5,
#     'spd':4,
#     'pit':8,
#     'per':1,
# })

# print(res)

with open("s1.mp3","wb") as f:
    for i in range(len(res)):
        f.write(res[i])
        print('写入第{}段{}'.format(i,res[i]))