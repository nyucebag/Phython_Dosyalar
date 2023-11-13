

def hello_func():
	print('hello function')


hello_func()	

def hello_func():
	return'hello function'


print(hello_func())	

print(hello_func().upper())	

def hello_func2(greeting, name='You'):

	return '{} {}  Function'.format(greeting,name) 
		 

print(hello_func2('Hellooo'))		 


def student_info(*args, **kwargs):
	print(args)
	print(kwargs)


courses=['Math', 'Art']	

info ={'name': 'Ali', 'age':'25'}

print(student_info(*courses,**info))	


mounth_days =[0,31,28,31,30,31,30,31,31,30,31,30,31]

def leap_year(year):
	return year % 4 == 0 and (year % 100  != 0 or year % 400 == 0)


def days_in_mounth(year, month):

	if not 1<= month < 13:
		print('invalid month')

	if month == 2 and leap_year(year):	
		return '29'

	return mounth_days[month]


print(days_in_mounth(2017,2))	