__author__ = 'cruser42'

def hash_func(x, mylen):
    return int(x**37) % mylen



x=[None, None, None, None, None, None, None, None, None, None]


# 10
mydict = {}
mylist = ['cat', 'dog', 'mouse']
mylist2 = [, 'pet', 'pest']

mydict['cat'] = None
mydict['dog'] = None
mydict['mouse'] = None

# print(mydict)

zipped_l = zip(mylist, mylist2)
print(zipped_l)
mydict = dict(zipped_l)

print(mydict)
if 'cat' in mydict:
    print('cat in mydict')

