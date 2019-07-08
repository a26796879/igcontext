import json
import jieba

data = open( "D:/Python Codes/igcontext/abc.json",'r').read()

#print (type(data))
jsload = json.loads(data)
#print (jsload[0]['context'])
print (type(jsload))
print (len(jsload))

context = []
'''
for text in range(len(jsload)):
    seg_list = jieba.cut(jsload[text]['context'].replace('\n',''), cut_all=False)
    context.append(seg_list)
'''
#print (context)
#allcontext = ''.join(context)
#print (allcontext)
li = jieba.cut(jsload[0]['context'], cut_all=False)
print (type("Default Mode: " + "/ ".join(li)))

#print("Full Mode: " + "/ ".join(seg_list))