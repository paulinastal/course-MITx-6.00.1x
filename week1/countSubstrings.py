count = 0

s = 'azcbobobegghakbobobl'
subs = 'bob'

for i in range(len(s)):
    if s[i:i+len(subs)] == subs:
        count += 1

print("Number of times bob occurs is: " + str(count))
    
            
    

