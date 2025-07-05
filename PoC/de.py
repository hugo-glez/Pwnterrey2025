def decode(par,v):

    v1 = ord(par[0])-65
    par = par[1:]
    #print(par)
    v2 = ""
    while len(par) >0 :
        v5 = par[0]
        v3 = ord(v5)-65
        v4 = ord(par[1])-65
        v2 = v2+ chr(v3*25+v4-v1-v)
        par = par[2:]
        #print(par)
        #print("."+v2)
    return v2


varss = open('data.txt','r').read().split("\n")[:-1]
dkey = 78
#print(varss)

ddata ={}

for va in varss:
    data = va.split('"')
    v1 = data[0].split("=")[0].strip()
    ddata[v1] = decode(data[1],dkey).replace("/","\/") #.replace("\\","-").replace('"','').replace('#','@')


keyss = ddata.keys()
nk = sorted(keyss,key=len,reverse=True)

for k in nk:
    #print("echo :",'sed -i s/'+k+'/\\"'+ddata[k]+ '\\"/ file.vbs')
    print('''sed -i 's/'''+k+'/\\"'+ddata[k]+ '''\\"/' file.vbs''')

