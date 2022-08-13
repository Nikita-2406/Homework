dict_fail = {}
with open('1.txt') as f1:
    f1_text = f1.read()
    f1.seek(0)
    dict_fail[len(f1.readlines())] = {'name': '1.txt', 'call': f1_text}
with open('2.txt') as f2:
    f2_text = f2.read()
    f2.seek(0)
    dict_fail[len(f2.readlines())] = {'name': '2.txt', 'call': f2_text}
with open('3.txt') as f3:
    f3_text = f3.read()
    f3.seek(0)
    dict_fail[len(f3.readlines())] = {'name': '3.txt', 'call': f3_text}
sorted(dict_fail.items())
dict_fail = sorted(dict_fail.items())
print(dict_fail)
for size, dict_ in dict_fail:
   name, call = dict_.values()
   print(name)
   print(size)
   print(call)