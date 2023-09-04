# l=[1,2,3,4,5,6,True,"deepankar",False]

# for i in l:
#     print(i)
#     print(type(i));

# x=100
# count=0

# while x!=0:
#     if x%5==0:
#         x=x/5
#         count+=1;
# print(count);

# l=[1,2,3,4,5,6,7,8,9,10,12,15,18,21,24,27,30,32,45,65,23,42,89,99,102,48,29,20]

# for i in l:
#     if i%3==0:
#         print(i ,"is divisible by 3")
#     else:
#         print(i,"not divisible by 3");

# for i in l:
#     if i%5==0:
#         print(i,"divisible by 5")
#     else:
#         print(i, "not divisible by 5");

# s="pwskills"
# print(s[2:7]);
# print(s[2::2]);
# print(s[::-1]);
# # print(s[1:4:-1]);
# # print(s[8:-1:-1]);
# print(s[-2::-1]);
# print(s[::-1]);
# # print(s[:-90:];) error
# print("deep" *4);
# print("deep"/4); error

l=[1,2,3,"deepankar",True]
# print(type(l));
# print(l[0])
# print(l[-1]);
# print(l[::-1]) #print in reverse direction
# print(l[::2]); #even index
# print(l[1::2]); #odd index
# s="pwskills"
# print(l+s); gives error not concatenate
# print(l[3]);
# print(type(l))
# print(l[3][0:4]);
# print(str(l[4])[0:2]);
# # print(l+5); gives error
# l1=[2,3,4,5];
# print(l+l1); #concatenate
# print(l1*3);
# print(len(l1));
# l.append(5);
# print(l)
# l.append("ashutosh") #it appends end of the list
# print(l);
# s="aman"
# l.append(s);
# print(l)
# l.append(l1); #nested list
# print(l);
# print(l[-1])
# print(l[-1][2]);
# #extend gives error in integers
# l.extend("deep");
# print(l)
# l.extend([2,3,4]); # its fine
# print(l)

# # at given index we insert data
# l1.insert(2,"maa");
# print(l1);
# l1.insert(2,[1,2,3,45]) #index,object
# print(l1);
# l1.insert(-1,34);
# print(l1); 
# l1.insert(0,23);
# print(l1);
# l1.pop(); #remove data from end by default index is -1
# print(l1);
# l1.pop(2);
# print(l1); #it takes index
# l1.remove(23);
# print(l1) # it removes the data
# # l1.remove(90) # not a part of the list it gives error
# # print(l1);
# l1[1].remove(45)
# print(l1);
# # l1[2].remove('a'); it gives error
# # print(l1);
# l1.append(21);
# print(l1);
# l1.reverse() #permanent reverse
# l1[::-1] # not a permanent reverse 
# l1=l1[::-1] # permanent reverse reassinged
# print(l1)

# l2=[2,3,4,2,1,0,5,7,4];
# l2.sort() #same data type
# print(l2)

# l3=["deepankar","ashutosh","aman"]
# l3.sort() # permanent change
# print(l3)
# print(l3.index("deepankar"))
# print(l3.count("aman"))

# s="deepankar"
# # s[0]='a';immutable
# # print(s); # gives error
# l3[0]=34; # reassinged
# print(l3)

# print(s.replace('d','a')); # it do not change original string
# print(s);

# tuples
# t=(2,3,2,4,"deepankar",23+4j,[1,2,3])
# print(type(t))
# print(t[0])
# print(t[::-1]) # original tuples is not change
# # t[0]="deep" # gives error,  immutable -->tuples
# # print(t);
# print(t.count(2));
# print(t.index(3))

# set

# s1={}
# print(type(s1)); #empty curly braces is dictionary

# s2={2,3,4,5}
# print(type(s2)) # it is a set

# s3={1,1,1,1,2,2,2,2,3,3,3,3,4,5,4,4,};
# print(s3) # it removes duplicate elements
# s4={122,121,345,122,121,222,221,23,421}
# print(s4)
# # it only removes  duplicate elements
# s4.add(3)
# print(s4);
# s4.remove(122)
# print(s4) # it does not define index
# it works on hashing 


#dictionary
# d={}
# print(type(d));
# #key will be uique
# d1={'key':"deepankar"}
# print(d1);
# d2={'name':"deepankar" , 'email':"@gmail.com" , "number":27}
# print(d2)

# # d3={234:"dee" , @:3}
# #it dives error not use special case character
# d3={234:"deepankar" , '_wer':"deo", True:23}
# print(d3[234]) #we use key to fetch the value
# print(d3[True]);
# print(d3["_wer"])
# d4={'name':"deepankar", 'mail_id':"@gmail.com" , 'name':"deep"}
# print(d4['name'])
# d5={"company":"pwskills", "courses":["web dev", "data science", "cpp"]}
# print(d5)
# print(d5['courses'][1])
# d6={"number":[2,23,34,32],"assingment":(1,2,3,3,4), "launch_date":{24,12,23}, "class_time":{"web_dev":12,"data-science":31,"cpp":19}}
# #list and tuples and set dictionary inside dictionary
# print(d6)
# print(d6['class_time'])
# print(d6['class_time']['cpp'])
# d6['mentor']=["deepankar", "ashutosh",'aman']
# print(d6)

# #delete
# del d6['number']
# print(d6)
# print(d6.keys())
# print(d6.values())
# print(d6.items()) #pairs of keys and values
# d6.pop('assingment') #give the key
# print(d6)
#dictionary is mutable

#or typecast to any data type
# marks=int(input("enter your marks: "))
# if marks>=80:
#     print("you will be a part of A0 BATCH")
# elif marks>=60 and marks<80:
#     print("you will be part of A1 batch")
# elif marks>=40 and marks<60:
#     print("you will be part of A2 batch")
# else:
#     print("you will be part of A3 batch")


# price=int(input("enter price: "))
# if price >1000:
#     print("i will not purchase")
#     if price >5000:
#         print("this is too much")
#     elif price <1000:
#         print("i will purchase")
# else:
#     print("not purchased")

# l=[1,2,3,4,5,6,7,8,9]
# l1=[]
# for i in l:
#     l1.append(i+1)

# print(l1)
l2=["deepankar", "ashutosh", "aman"]
l3=[]
for i in l2:
    l3.append(i.upper())
print(l3)

l4=[1,2,3,4,5,"deepankar", 23.23]
l5_num=[]
l6_str=[]

for i in l4:
    if type(i)==int or type(i)==float:
        l5_num.append(i)
    else:
        l6_str.append(i)

print(l5_num)
print(l6_str)




































