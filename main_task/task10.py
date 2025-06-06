prods = [['omo','30kshs','300'], ['milk','50kshs','200'],['bread','45kshs','359'], ['coffee','5kshs','79']]
sum=0
for r in prods:
    r[2]=int(r[2])
    sum=sum+r[2]
print(sum)
