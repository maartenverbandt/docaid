file = open("extra_informatie_voor_in_computerprogramma.html","r")
text = file.read();

ulpos = [0]
ulepos = [0]

# find all matches of <ul></ul>
while(ulpos[-1] >= 0):
    ulpos.append(text.find('<ul>',ulpos[-1]+1))

ulpos = ulpos[1:-1];

while(ulepos[-1] >= 0):
    ulepos.append(text.find('</ul>',ulepos[-1]+1))

ulepos = ulepos[1:-1];

print ulpos
print ulepos
print len(ulpos), len(ulepos)

culpos = 0
culepos = 0
ulcounter = 0
pbegin = 0
uls = []

while culpos < len(ulepos):
    if ulpos[culpos] < ulepos[culepos]:
        if culpos == culepos:
            pbegin = culpos
        culpos += 1
    else:
        culepos += 1
        if culpos == culepos:
            uls.append(text[ulpos[pbegin]:(ulepos[culepos-1]+5)])

print uls[0]
print uls[1]
print uls[2]

#    ulepos = text.find('</ul>',)
#    
#    else:
#        ulcounter -= 1
#        assert(ulcounter >= 0,'something went wrong with ul-/ul matching')
#        if ulcounter == 0
#            pend = ulepos
            
    
    
    
    
    
#    cpointer += 1
