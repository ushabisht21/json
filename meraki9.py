import json
dict={
    "shopping_list":
        { 
            "chaco":"15",
            "Biscuits":"50",
            "Diary_milk":"30",
            "ice_cream":"20",
        } 
}
# shopping_list= open("new file.json", "w")
  
# json.dumps(dict, shopping_list, indent = 4)
  
# shopping_list.close()
out_file = open("meraki.json", "w")
  
json.dump(dict, out_file, indent = 6)
  
out_file.close()