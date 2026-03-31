#list is mutable so we can change the any variable
'''student1=["sandhy","ml",20,43]
print(type(student1))
student1[1]="al"
print(student1)
student2=["kani","ml",19,39]
s=student1+student2
print(s)


#append
a=[1,2,3,4,5,6]
a.append(7)
print(a)


#copy
c=a.copy()
print(c)


#extend
a.extend(c)
print(a)


#count
print(a.count(5))


#index
print(a.index(7))


#insert
a.insert(12,99)
print(a)


#sort
a.sort()
print(a)

#reverse
a.reverse()
print(a)


#pop
a.pop()
print(a)

#tuple is immutable we can not change any variable in tuple.so we use the list
a="apple","sweet","red",100,"strawberry","sweet","red",120
print(type(a))

#index
print(a.index("red"))

#count
print(a.count("red"))


#set is unordered items.set remove the duplicate element.set is mutable


b={11,22,33,44,55,66,77}
d={88,99,100,11,22,10}
#add
b.add(88)
print(b)

#copy
c=b.copy()
print(c)

#intersection
print(b.intersection(d))

#difference
print(b.difference(d))

#symmetric
print(d.symmetric_difference(b))

a={1,2,3,4,5,6}
c={3,6}

#issubset
print(c.issubset(a))

#issuperset
print(a.issuperset(c))
print(c.issuperset(a))

#union
print(b.union(d))

#isdisjoint
print(a.isdisjoint(c))

#discard
print(a.discard(c))

#remove
print(a.remove(c))'''

#dictionary is have the key and pairs
e={1:11,2:22,3:33,4:44,5:55}
#items
print(e.items())

#keys
print(e.keys())

#get
print(e.get(4))


#pop
print(e.pop(2))

#update
e.update({4:88})
print(e)

#fromkeys
n={"s","a","n","d"}
k="name"
fk=dict.fromkeys(n,k)
print(fk)
