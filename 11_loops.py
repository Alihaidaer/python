#while and for loop
#while loops
# x=0
# while x<5:
#     print(x)
#     x=x+1

# # for loop
# for x in range(5,10):
#     print(x)

#array 
days=("sun","mon","thu","wed","tus","fri","sat")

for d in days:
    # if (d=="thu"):break  #loops break  when condition is met

    if (d=="wed"):continue #loop continue but condition we applied is skip
    print(d)
