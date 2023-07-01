def hello():
    print('Hello User')

def pack(str1, str2, str3):
    return[str1,str2,str3]

def eat_lunch(list_items):
    if len(list_items) == 0:
        print('My lunchbox is empty')
    else:
        for i in range(len(list_items)):
            if i == 0:
                print(f'First I eat {list_items[0]}')
            else:
                print(f'Next I eat{list_items[i]}')


print(hello())
print(pack('Sea','Lake','River'))
print(eat_lunch([]))
#print(eat_lunch(['Chicken']))
print(eat_lunch(['Candy','Chicken','Apple','Rice']))

