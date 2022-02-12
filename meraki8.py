text='{  "Name": "Abhishek","Designation":"CEO of navgurukul","Gender": "male","Age" :29}'
out_file = open("meraki.json", "w")
text.dump(text, out_file, indent = 4)
out_file.close()