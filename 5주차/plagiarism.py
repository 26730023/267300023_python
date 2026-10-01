s1 = input("첫 번째 문자열:")
s2 = input("두 번째 문자열:")

s1 = s1.lower()
s2 = s2.lower()

list1 = s1.split(" ")
list2 = s2.split(" ")

total = len(list1)
n = len(list(set(list1) & set(list2)))

print(f"\n표절률 = {100*n/total}")
