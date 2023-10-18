
#Merging dictonaries using update function
dict1 = {'name':"anushka", 'age':24}
dict2 = {'location':"haldwani", 'gender':"female"}
dict1.update(dict2)
print(dict1)

#Merging the dictonaries using a pipe operator 
dict1 = {'name':"anushka", 'surname':"mittal"}
dict2 = {'email': "anushkamittal0@gmail.com", 'gender':"female"}
print(dict1|dict2)
