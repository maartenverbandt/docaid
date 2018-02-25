# -*- coding: utf-8 -*-

import csv

# parse the metadata file
file = open("extra_informatie_voor_in_computerprogramma.html","r")
text = file.read()
text = text.replace('\n','').replace('\n','').replace('\"','\\\"').replace('\\\\','\\\\\\\\').replace("ë",'&euml').replace("ï",'&iuml').replace("ö",'&ouml').replace("ä",'&auml').replace("ü",'&uuml')
# text = text.replace('\n','').replace('\n','')
ulpos = [0]
ulepos = [0]

# find all matches of <ul></ul>
while(ulpos[-1] >= 0):
    ulpos.append(text.find('<ul>',ulpos[-1]+1))

ulpos = ulpos[1:-1];

while(ulepos[-1] >= 0):
    ulepos.append(text.find('</ul>',ulepos[-1]+1))

ulepos = ulepos[1:-1];
assert(len(ulpos)==len(ulepos))

culpos = 0
culepos = 0
ulcounter = 0
pbegin = 0
uls = []
key = ('Anamnese','KO','TO','Hyperlink')
keycount = 0

while culepos < len(ulepos):
    print culpos, culepos
    print len(ulpos), len(ulepos)
    if (culpos < len(ulpos)) and (ulpos[culpos] < ulepos[culepos]):
        if culpos == culepos:
            pbegin = culpos
        culpos += 1
    else:
        culepos += 1
        if culpos == culepos:
            if pbegin == 0:
                assert text.find(key[keycount],0,ulpos[pbegin])>0 , "%r" % text[0:ulpos[pbegin+1]]
            else:
                assert (text.find(key[keycount],ulepos[pbegin-1],ulpos[pbegin])>0) , "%r" % text[(ulepos[pbegin-1]-30):(ulpos[pbegin+1]+30)]
                
            keycount = (keycount + 1) % 4
            uls.append(text[ulpos[pbegin]:(ulepos[culepos-1]+5)])

# construct ziektes.js
js_file = open("ziektes.js","w+")
js_file.write("var ziektes = [];\r\n")
counter = 0
r = 0

symptomen = (('koorts',2), ('duur',2), ('leeftijd',3), ('gewicht',2), ('uitgeslapen',2), ('luchtwegklachten',2), ('keelpijn',2), ('angst',2))   

csvfile = open('ziektes.csv', "rb")
csvreader = csv.reader(csvfile, delimiter=',')

#print sum(1 for row in csvreader), ' rows in csv'
print len(uls) 
print uls[-1]

for row in csvreader:
    js_file.write('ziektes[%i] = {' % counter)
    
    # naam van ziekte
    name = row[r];
    #print int(row[r+1])
    if int(row[r+1]) == 1:
        name = '<b>' + name + '</b>'
    elif int(row[r+1]) == -1:
        name = '<i>' + name + '</i>'
    
    #print name
    js_file.write('name:\"' + name + '\", belang:' + row[r+1])
    r = r + 2
    
    for symptoom in symptomen:
        js_file.write(', ' + symptoom[0] + ':[' + row[r])
        for i in range(1,symptoom[1]):
            js_file.write(',' + row[r+i])
        js_file.write(']')
        r = r + symptoom[1]
    
    js_file.write(', anamnese:\"' + uls[4*counter] + '\", KO:\"' + uls[4*counter+1] + '\", TO:\"' + uls[4*counter+2] + '\", hyperlink:\"' + uls[4*counter+3] + '\"')
    
    #end line
    js_file.write('};\r\n')
    
    # assertion to avoid errors in conversion
#    print r, len(row)
    assert (r == len(row))
    counter = counter + 1
    r = 0
    
js_file.close()
csvfile.close()
print 'conversion done!'
