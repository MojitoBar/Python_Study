# arr = str(input())
# count = 0
# for i in range(len(arr)):
#     if("b" == arr[i]):
#         if(i+1 < len(arr) and arr[i+1] == "o"):
#             if(i+2 < len(arr) and arr[i+2] == "b"):
#                 count+=1
# print(count)

# cus = []
# n = 0
# while(True):
#     print("대기자 추가: A")
#     print("대기자 호출: C")
#     z = input("명령어(A/C): ")
#     if(z == "A"):
#         cus.append(input("대기자 성명: "))
#         n += 1
#         print("==대기자 명단==")
#         for i in range(n):
#             print(cus[i])
#     elif(z == "C"):
#         print("호출고객: " + cus[0])
#         del cus[0]
#         n -= 1
#         print("==대기자 명단==")
#         for i in range(n):
#             print(cus[i])
#     elif(z == ""):
#         break
#     else:
#         print("잘못입력함 ㅅㄱ")
#
# n = input("input: ")
# count = 0
# for i in range(len(n)-2):
#     if n[i] == "b":
#         if n[i:i+3] == "bob":
#             count += 1
# print("Number of times bob occurs is: %d" %count)

# ---------------------------------------------------------
# ------------------ 파이썬 중간고사 ------------------------
# ---------------------------------------------------------

# # 2번 문제
# name = input("이름 : ")
# print("이름 : " + name)
#
# # 3 ~ 4번 문제
# a = 10
# b = 4
# c = 4.0
#
# result1 = a/b
# print(result1)
#
# remainder = a%b
# print(remainder)

# # 5 ~ 7번 문제
# s = "가나다라마바사아자차카타파하"
#
# print(s[3:10:2])
# print(len(s))
# print(s[10::-1])

# # 12번 문제
# def max(*a):
#     max_n = 0
#     max_n = a[0]
#     for i in a:
#         if(max_n < i):
#             max_n = i
#     return max_n
#
# print(max(2, 3, 6, 4, 8, 9))
#
# def min(*a):
#     min_n = a[0]
#     for i in  a:
#         if(min_n > i):
#             min_n = i
#     return min_n
# print(min(4,7,3,5,7))

# # 13번 문제
# n = input("input : ")
# count = 0
# for i in range(len(n) - 2):
#     if(n[i:i+3] == "bob"):
#         count += 1
# print("Number of times bob occurs is : %d" %count)

# # 14번 문제
# list = []
# while(True):
#     print("대기자 추가 : A")
#     print("대기자 호출 : C")
#     n = input("명령어(A/C) : ")
#     if (n == "A"):
#         name = input("대기자 성명 : ")
#         list.append(name)
#         for i in list:s
#             print(i)
#     elif (n == "C"):
#         print("호출 고객 : " + list[0])
#         del list[0]
#         for i in list:
#             print(i)
#     elif (n == ""):
#         break
#     else:
#         print("A 또는 C를 입력해주세요. 마치려면 아무것도 입력하지 말고 엔터를 처주세요.")

# def is_prime(n):
#     for i in range(2, n):
#         if(n % i == 0):
#             return False
#         elif(i==n-1):
#             return True
#
# print(is_prime())

# def sum_digit(n):
#     sum = 0
#     while(n!=0):
#         sum += n % 10
#         n = n //10
#     return sum
#
# print(sum_digit(12334))

# a = input("단어입력:")
# list = []
# list.append(a[0])
# for i in a:
#     for j in range(len(list)):
#         if (i == list[j]):
#             break
#         elif(j == len(list) - 1):
#             list.append(i)
# list.sort()
# str = ""
# for i in list:
#     str = str + i;
# print("입력 받은 단어:" + a)
# print("단어에 포함된 알파벳" + str)

# M = int(input("M:"))
# N = int(input("N:"))
# list = []
# for i in range(M, N + 1):
#     for j in range(N + 1):
#         if(j * j == i):
#             list.append(i)
# min = 0
# sum = 0
# list.sort()
# min = list[0]
# for i in list:
#     sum += i
# print("합:" + str(sum))
# print("최솟값" + str(min))

def r_product(x, y):
    if y > 1:
        return x + r_product(x, y - 1)
    else:
        return x

print(r_product(3, 4))