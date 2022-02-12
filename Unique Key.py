dict={
"a":1,
"a":2,
"a":3,
"a":4,
"b":1,
"b":2
}
a={}
for i in dict:
    if i not in a:
        a.update(dict)
print(a)