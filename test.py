l = ['[1, 2, 322]']
j = l[0][1:len(l[0])-1]
o = []
k = ""
for i in range(0, len(j)):
    if j[i] == ",":
        o.append(k)
        k = ""
    elif i == len(j) - 1:
        k += j[i]
        o.append(k)
    elif j[i] == " ":
        continue
    else:
        k += j[i]

res = []
for elt in o:
    res.append(int(elt))

print(res)
