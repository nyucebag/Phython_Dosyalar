student = {'name':'John' , 'age' :'25', 'courses':['History', 'CompSci']}

print(student)

print(student.get('name'))

print(student.get('phone','Not found'))


student['phone']='555-55-55'

print(student.get('phone'))

#student['name']='Jane'
#print(student)

student.update({'name':'Jane', 'age':'31', 'phone':'666-66-66'})

print(student)

#del student['age']  

#print(student)


#name =student.pop('name')

#print(name)


print(student.keys())



for key in student:
	print(key)



for key, value in student.items():
	print(key, value)
