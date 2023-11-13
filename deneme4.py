
language='Java'

if language == 'Python':
	print('Language is python')
elif language == 'Java' :
	print('Language is Java')

else:
	print('No match')


a= [1,2,3]	

b=[1,2,3]


b=a
print(id(a))
print(id(b))

print (a is b)