import json
def is_complex_num(objct):
    if '__complex__' in objct:
        return objct
complex_object =json.loads('{"__complex__": true, "real": 4, "img": 5}', object_hook = is_complex_num)
simple_object =json.loads('{"real": 4, "img": 3}', object_hook = is_complex_num)
meraki_file= open("meraki4.json", "w")
  
json.dump(complex_object, meraki_file, indent = 6)
  
meraki_file.close()