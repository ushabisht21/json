import json
dict1 =  { "Name":"usha", "Class":"I", "Age":19, 
"home":"nainital"}


my_file  = open("usha.json", "w")
  
json.dump(dict1, my_file, indent = 6)
  
my_file.close()