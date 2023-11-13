
courses=['History','Math','Physics','Geometry']

print(courses[1])

print(courses[0:2])

#courses.append('Art')

#print(courses)

#courses.insert(0,'Art')

#print(courses)

courses_2=['Art','Education']

#courses.insert(0,courses_2)
#print(courses)

courses.extend(courses_2)
print(courses)


#courses.remove('Math')

#courses.pop()


courses.reverse()

courses.sort()

print(courses)


nums = [1,5,2,4,3]

print(nums)

nums.sort()

print(nums)

nums.sort(reverse=True)

print(nums)

sorted_nums =sorted(nums)

print(sorted_nums)

print(min(nums))

print(max(nums))

print(sum(nums))


print(courses.index('Math'))

print('Math' in courses)

for item in courses :
	print(item)


for index,course in enumerate(courses) :
	print (index, course)


for index,course in enumerate(courses, start=1) :
	print (index, course)

course_str=' - '.join(courses)

print(course_str)


cs_courses = {'History', 'Math', 'Physics', 'CompSci'}

art_courses= {'History' , 'Math', 'Art','Design'}

print(cs_courses.intersection(art_courses))

print(cs_courses.difference(art_courses))

print(cs_courses.union(art_courses))


empty_list= list()

empty_tuple = tuple()

empty_set = set()