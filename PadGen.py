'''
This is a cryptographically secure random number generator that uses the urandom to generate values for a one-time pad.
A pad must be generated before a client can connect to the server.
'''
import crpyto_random
import pickle

keys = []
print('      One-Time Pad Generator')
print('Values are Cryptographically Secure')
print('-----------------------------------')
y = raw_input('Number: ')
y = int(y)

for x in range(0, int(y)):
    z = crpyto_random.randint()
    z = z + 1
    keys.append(z)
    print(str((float(x)/float(y) * 100)) + ' %')
print('100 % - DONE!')
print('Writing Pad to crypto.pad')
f = open('crypto.pad', 'w')
pickle.dump(keys, f)
print('Done!')
