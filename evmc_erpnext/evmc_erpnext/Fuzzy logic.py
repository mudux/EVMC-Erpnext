from collections import defaultdict
import difflib

atxt="ali mohamud amin"
btxt="ali karani amin"

aarr=atxt.split()
barr=btxt.split()
alen=len(aarr)
blen=len(barr)
rates=defaultdict(dict)
length=0
maximum=0.0
high=0.0
if alen>=blen:
    for aelm in aarr:
        high=0.0
        for belm in barr:
            seq=difflib.SequenceMatcher(None,a=aelm.lower(),b=belm.lower())
            d=seq.ratio()*100
            d=round(d,1)
            rates[aelm][belm]=d
        for key,value in rates[aelm].items():
            if value>high:
                high=value
        maximum = maximum + high
        print(high)
    length = alen
if blen>alen:
    for belm in barr:
        high=0.0
        for aelm in aarr:
            seq=difflib.SequenceMatcher(None,a=aelm.lower(),b=belm.lower())
            d=seq.ratio()*100
            d=round(d,1)
            rates[belm][aelm]=d
        for key,value in rates[belm].items():
            if value>high:
                high=value
        maximum = maximum + high
        print(high)
    length = blen
maximum = maximum/length
print(str(rates))
print(str(maximum))