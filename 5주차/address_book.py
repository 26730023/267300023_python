contacts = {}

while True:
    print("1. 연락처 추가")
    print("2. 연락처 삭제")
    print("3. 연락처 검색")
    print("4. 연락처 출력")
    print("5. 종료")

    menu = input("메뉴 항목을 선택하시오: ")

    if menu == "1":
        name = input("이름: ")
        phone = input("전화번호: ")
        contacts[name] = phone

    elif menu == "2":
        name = input("삭제할 이름: ")
        if name in contacts:
            del contacts[name]

    elif menu == "3":
        name = input("검색할 이름: ")
        if name in contacts:
            print(name, "의 전화번호:", contacts[name])

    elif menu == "4":
        for name, phone in contacts.items():
            print(name, "의 전화번호:", phone)

    elif menu == "5":
        break
