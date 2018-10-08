import requests

url = 'https://api.ownthink.com/slu?spoken=厦门明天会不会下雨'      # 口语理解API
sess = requests.get(url) # 请求

text = sess.text # 获取返回的数据
print(text) 

slu = eval(text) # 转为字典类型
print(slu)

