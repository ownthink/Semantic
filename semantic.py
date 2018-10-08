import requests

url = 'https://api.ownthink.com/slu?spoken=厦门明天会不会下雨'      # 口语理解API
sess = requests.get(url) # 请求

text = sess.text # 获取返回的数据
print(text) 

slu = eval(text) # 转为字典类型
print(slu)

data = slu['data']

# 中文分词
cws = data['词法分析']['中文分词']
print(cws)

# 词性标注
pos = data['词法分析']['词性标注']
print(pos)

# 命名实体识别
ner = data['词法分析']['实体识别']
print(ner)

# 领域分类
domain = data['semantics'][0]['domain']
print(domain)

# 槽填充
slot = data['semantics'][0]['slot']
print(slot)

# 意图识别
intent = data['semantics'][0]['intent']
print(intent)



