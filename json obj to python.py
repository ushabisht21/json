import json


json_obj='{"name":"johan","age":30}'
python_obj=json.loads(json_obj)
print(python_obj)


json_obj='{"album_title" : "Yellow Submarine"}'
python_obj=json.loads(json_obj)
print(python_obj)

