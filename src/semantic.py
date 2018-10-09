import requests

class Analysis:
	def __init__(self, text):
		self.data = None
		if text=='' or type(text) != str:
			return None
		url = 'https://api.ownthink.com/slu?spoken=%s'%text
		sess = requests.get(url)
		text = sess.text
		slu = eval(text)
		
		self.data = slu['data']
		
	def analysis(self):

		# 中文分词
		self.cws = self.data['词法分析']['中文分词']
		
		# 词性标注
		self.pos = self.data['词法分析']['词性标注']
		
		# 命名实体识别
		self.ner = self.data['词法分析']['实体识别']
		
		# 领域分类
		self.domain = self.data['semantics'][0]['domain']

		# 槽填充
		self.slot = self.data['semantics'][0]['slot']

		# 意图识别
		self.intent = self.data['semantics'][0]['intent']

		return self.data
		
		
		