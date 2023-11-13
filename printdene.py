message='Hello World'
print(message)

print(len(message))

print(message[0])

print(message[0:5])
print(message[6:])


print(message.lower())

print(message.upper())

print(message.count("l"))

print(message.find("World"))

print(message.find("Universe"))

new_message=message.replace('World','Universe')

print(new_message)

greeting='Hello '
name='Nuray'

message_2=greeting+name
print(message_2)

message_3 ='{}, {} . Welcome ! '.format(greeting,name)

print(message_3)

message_3y=f'{greeting} , {name.upper()} . Welcome !'

print(message_3y)


print(dir(name))


print(help(str))

print(help(str.lower))

