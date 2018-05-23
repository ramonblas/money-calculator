#para contar los gastos automaticamente del txt de wapp
import re
import json
import csv

fhand = open('_chat.txt')

count_k = []
count_v = []
count_d = {}

for line in fhand:
    line = line.rstrip()
    #x = re.findall('([0-9])*\$([0-9]+.*)', line)
    #v = re.findall('([0-9]*)\$([0-9]*).*', line)
    
    #if len(v)>0: print v
    
    k = re.findall('\$[0-9]+\S*(.+)', line)
    if len(k) > 0:
        #print k
        #v2 = float(v[0])
        count_k.append(k[0])
        
    v = re.findall('\$([0-9]+)', line)
    if len(v) > 0:
     #   print v
        v2 = float(v[0])
        count_v.append(v2)
    
count_d = dict(zip(count_k, count_v))


formato = raw_input('Por default el archivo se crea en "csv", a menos que pongas "json": ')
if formato != 'json':
    with open('cuenta_mes.csv', 'wb') as f:
        w = csv.DictWriter(f, count_d.keys())
        w.writeheader()
        w.writerow(count_d)

else:
    with open('cuenta_mes.json', 'w') as fp:
        json.dump(count_d, fp)

print 'Suma Total del mes en Pesos', sum(count_v)