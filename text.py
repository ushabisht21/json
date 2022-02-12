import json 
dic ={"name":"abhishek","designation":"ceo of navgurukul","gender":"male","age":29}
a=json.dumps(dic,indent=2)
with open("text.text.json","w")as f:
    f.write(a)
    f.close()
f=open("text.text.json","r")
b=f.read
print(a)

