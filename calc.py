def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# 사용자 입력 받기
num1 = float(input("첫 번째 숫자를 입력: "))
num2 = float(input("두 번째 숫자를 입력: "))

# 연산 선택
operation = input("+ or - ? : ")

if operation == "+":
    print(f"결과: {add(num1, num2)}")
elif operation == "-":
    print(f"결과: {subtract(num1, num2)}")
else:
    print("올바른 연산자를 입력하세요!")
