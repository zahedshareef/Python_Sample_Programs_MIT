# lecture 3.1, slide 2

# repetitive addition

print "Enter Number to find square "
x=int(raw_input('Input:'))
  
ans = 0
itersLeft = x
while (itersLeft != 0):
    ans = ans + x
    itersLeft = itersLeft -1
print(str(x) + '*' + str(x) + ' = ' +str(ans))
