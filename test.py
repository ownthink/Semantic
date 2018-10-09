from src.semantic import Analysis

if __name__=='__main__':
	
	text = '厦门明天会不会下雨'

	slu = Analysis(text)
	
	data = slu.analysis()  #解析
	print(data) #总的结果
	
	print('--------------------------')
	
	print(slu.cws)#分词
	
	print(slu.pos)
		
	print(slu.ner)
	
	print(slu.domain)
	
	print(slu.intent)
	
	print(slu.slot)
	
	