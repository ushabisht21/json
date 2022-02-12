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
shopping= open("shopping_list", "w")
  
json.dump(dict, shopping, indent = 6)
  
shopping.close()