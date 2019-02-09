#!/usr/bin/env python3

# this is my first script
message = ''
for x in (1,2,3,4,5):

    if x > 4:
        print("hello")
        message = 'x is big'
    else:
        print(x)
        message = 'x is small'
    print(message)

print('All Done')
