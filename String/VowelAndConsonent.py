# N= int(input( ))
# vowels_list = "aeiouAEIOU"

# for _ in range(N):
#     s = input("Enter string: ")
#     vowels = 0
#     consonants = 0

#     for ch in s:
#         if ch.isalpha(): 
#             if ch in vowels_list:
#                 vowels += 1
#             else:
#                 consonants += 1

# print(vowels, consonants) 












# sum of n natural number
# n=int(input())
# sum=0
# for i in range(1,n):
#     sum+=i
# print(sum)


def sum_n(N):
    if N==1:
        return 1
    return(sum(N-1)+N)
N=int(input())
print(sum_n(N))

# calculate factorial of n
def fact_n(N):
    if N==0:
        return 1
    return(fact(N-1)*N)

