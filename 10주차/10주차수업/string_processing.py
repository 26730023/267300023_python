phrase = input("문자열을 입력하시오: ")
acronym = ""

for word in phrase.upper().split():
    acronym += word[0]

print(acronym)

address = input("이메일 주소를 입력하시오: ")
user_id, domain = address.split("@")

print("아이디:", user_id)
print("도메인:", domain)

s1 = input("첫 번째 문자열: ")
s2 = input("두 번째 문자열: ")

common = list(set(s1) & set(s2))
print("공통적인 글자:", common)
