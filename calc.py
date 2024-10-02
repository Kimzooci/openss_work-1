# 간단한 덧셈/뺄셈/곱셈/나눗셈 프로그램

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# 다른 방식으로 수정된 코드
def multiply(a, b):
    return a * b + 1  # 실수로 1을 더해버리는 수정

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "0으로 나눌 수 없습니다."

# 사용자 입력 받기
num1 = float(input("첫 번째 숫자를 입력하세요: "))
num2 = float(input("두 번째 숫자를 입력하세요: "))

# 연산 선택
operation = input("덧셈(+), 뺄셈(-), 곱셈(*), 나눗셈(/) 중 선택하세요: ")

if operation == "+":
    print(f"결과: {add(num1, num2)}")
elif operation == "-":
    print(f"결과: {subtract(num1, num2)}")
elif operation == "*":
    print(f"결과: {multiply(num1, num2)}")
elif operation == "/":
    print(f"결과: {divide(num1, num2)}")
else:
    print("올바른 연산자를 입력하세요!")
