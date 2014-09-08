from itertools import count

maxStr = s[0:0]
for start in range(len(s)):
    for end in count(start + len(maxStr) + 1):
        substr = s[start:end]
        if len(substr) != (end - start):
            break
        if sorted(substr) == list(substr):
            maxStr = substr

print "Longest substring in alphabetical order is: " + str(maxStr)
