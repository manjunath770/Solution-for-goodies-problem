x=open('sample_input.txt','r')
m=x.readline().split(' ')[3]
m=int(m)
print(m)
number=[3,4,5,6,7,8,9,10,11,12,13,14,15]
d={}
a_list=[]
for pos,line in enumerate(x):
    if pos in number:
        line=line.rstrip('\n')
        a,b=line.split(':')
        b=b.replace(" ","")
        print(b)
        a_list.append(b)
        d[b]=a
print(d)

for i in range(len(a_list)):
    a_list[i]=int(a_list[i])

a_list.sort()
print(a_list)

min_value=a_list[9]
i=0
j=m-1
while(j<len(a_list)):
    value=a_list[j]-a_list[i]
    if(value < min_value):
        min_value=value
        start=i
        end=j
    i=i+1
    j=j+1
print(min_value,start,end)

y=open("sample_output.txt",'w')
y.write("Here the goodies selected for distribution are:\n")
y.write('\n')

for i in range(start,end+1):
  s=str(a_list[i])
  y.write(d[s])
  y.write(": ")
  y.write(s)
  y.write("\n")
y.write("\n")
y.write("And the difference between the chosen goodie with highest price and the lowest price is ")
y.write(str(min_value))
y.close()



        

