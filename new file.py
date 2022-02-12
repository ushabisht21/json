import json
dict1={"name":"usha","age":42}

out_file = open("new file.json", "w")
  
json.dump(dict1, out_file, indent = 4)
  
out_file.close()

