data, name, room, idno, hostel, sex = [], [], [], [], [], []

help_text = '''This bot can search details of students enrolled \
before 2016.
Usage(3 ways)-
1. <name>
2. i <id or its part>
3. h <hostel_code room no.>

egs.
myName
firstname last_name
partial_na
h rm 9999
h 8888
i 2014A0PS999
i 999'''


with open('students.csv') as f:
    for line in f:
        data.append(line)
        n,r,i,h,s=line.split(',')
        name.append(n)
        room.append(r)
        idno.append(i)
        hostel.append(h)
        if s==0:
            sex.append('Female')
        else:
            sex.append('Male')

def nameSearch(n):
    results = []
    ns = n.split()
    for pos, nam in enumerate(name):
        for part in ns:
            if part.lower() not in nam.lower():
                break
        else:
            results.append(pos)
    return results


def idSearch(n):
    results=[]
    for pos, ids in enumerate(idno):
        if n.upper() in ids:
            results.append(pos)
    return results

def hroom(n):
    h, r = "", ""
    parts=n.split()
    results = []
    if len(parts)==2:
        h=parts[0]  # Hostel
        r=parts[1]  # Room no
    else:
        if parts[0].isdigit():
            r = parts[0]
        else:
            h= parts[0]
    if r:
        for pos, rns in enumerate(room):
            if r in rns:
                if h:
                    if h.lower()==hostel[pos].lower():
                        results.append(pos)
                else:
                    results.append(pos)
    else:
        for pos in range(len(hostel)):
            if h.lower()==hostel[pos].lower():
                results.append(pos)
    return results

#ive it a query it will give you result
def main(query):
    results=[]
    if query=='/start' or query=='/help':
        results.append("help")
        return results


    if query[0].lower()=='h' and (query[1]==" " or query[1].isdigit()):
        results = hroom(query[1:].strip())
    elif query[0].lower()=='i' and (query[1]==" " or query[1].isdigit()):
        results = idSearch(query[1:].strip())
    elif query[0].isalpha() and query[1].isdigit():
        maph = {'r':'rm', 'b':'bd', 'm':'mr', 'c':'cvr'}
        if query[0].lower() not in maph:
            return []
        results = hroom(maph[query[0]] + " " + query[1:].strip())
    else:
        results = nameSearch(query.strip())
    return results


def get(results):
    if len(results)==0:
        return "No result."
    else:
        s=""
        if results[0]=="help":
            return help_text

        for pos, i in enumerate(results):
            if pos!=0:
                s+="--------------\n"
            s+="Name-%s\nRoom-%s %s\nId-%s\n" %(name[i], hostel[i], room[i], idno[i])
            if pos==10:
                break
        return s

