__author__ = 'AGN'

a_i=4
b_i=6

a_f=3.14
b_f=5.62

print ("Integer a: {} divided by b: {} is: {} ".format(a_i,b_i, a_i/b_i))

print ("Float a:{} divided by b:{} is: {} ".format(a_f,b_f, a_f/b_f))

print ("Integer a: {} divided by Float b: {} is: {} ".format(a_i,b_f, a_i/b_f))

# the act of converting an integer into a float in the following is called casting
print ("Float a: {} divided by Integer b: {} is: {} ".format(a_i,b_i, a_f/b_i))

# Binary Representation sys.maxint

# Numerical precision
# Machine episolon np.finfo(float).eps anything less than machine episolon is considered 0
# Python automatically handels precision

