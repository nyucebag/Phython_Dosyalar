import os

from datetime import datetime

#print(os.getcwd())

#os.rmdir('PythonDeneme2')


# mod_time=os.stat('deneme2.py').st_mtime

# print( datetime.fromtimestamp(mod_time))

 
# print(os.path.splitext('deneme2.py'))


# f= open('test.txt','r')

# print(f.name)

# f.close()

with open('test.txt', 'r') as f:
	# f_contents=f.read()
	# print(f_contents)

	for linez in f:
		#print(linez, end='')
		
		size_to_read=10
		f_contents=f.read(size_to_read)


		while len(f_contents) > 0:

			print(f_contents, end='*')
			f_contents=f.read(size_to_read)

with open('test2.txt','w') as f:
	f.write('test')
	f.seek(0)
	f.write('r')


with open('european-shorthair.jpg','rb') as rf:

	with open('european-shorthair_copy.jpg','wb') as wf:
			# for line in rf:
			# 	wf.write(line)	
		chunk_size=4096
		rf_chunk=rf.read(chunk_size)

			
		while len(rf_chunk) > 0 :
			wf.write(rf_chunk)
			rf_chunk=rf.read(chunk_size)