nums = [1,2,3,4,5]

# V1
for num in nums:
    print(num)


#V2
for num in nums:
    if num == 3:
        print("Found!")
        continue
    print(num)

#V3
for num in nums:
    for letters in 'abc':
     print(letters, num)


for i in range(10):
   print(i)


#WHILE LOOP
x = 0
while x < 5:
   print(x)
   x += 1