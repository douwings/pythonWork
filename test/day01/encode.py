import urllib.parse

url = 'http://www.baidu,com/index.html'

# 假设参数有 name age sex height
name = 'ziyi'
age = 24
sex = 'man'
height = '180'

data = {
    'name': name,
    'age': age,
    'sex': sex,
    'height': height,
}


query_string = urllib.parse.urlencode(data)

print(query_string)
# lt = []
# for k, v in data.items():
#     lt.append(k + '=' + str(v))
# query_string = '&'.join(lt)

url = url + '?' + query_string

print(url)
