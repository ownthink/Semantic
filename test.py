from src.semantic import Analysis

if __name__=='__main__':
	
	text = '厦门明天会不会下雨'

	slu = Analysis(text)
	
	data = slu.analysis()  #解析
	print(data) #总的结果
	
	print('--------------------------')
	
	print(slu.cws) #分词
	
	print(slu.pos) #词性标注
		
	print(slu.ner) #命名实体识别
	
	print(slu.domain) #领域分类
	
	print(slu.intent) #意图识别
	
	print(slu.slot) #槽填充
	
	