i = 99
for i in range(100, 1, -1):
    print("""{0} bottles of beer on the wall, {1} bottles of beer.
Take one down and pass it around, {2} bottles of beer on the wall.""".format(i, i, i-1))
if(i==2):
    print("""{0} bottle of beer on the wall, {1} bottle of beer.
Take one down and pass it around, no more bottles of beer on the wall.""".format(i-1, i-1))
print("""No more bottles of beer on the wall, no more bottles of beer on the wall
Go to the store and buy some more,  bottles of beer on the wall.""")
