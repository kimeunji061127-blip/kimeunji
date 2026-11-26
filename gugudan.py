# 단을 입력하면 구구단을 출력하는 함수!
def gugudan():
    x = int(input("몇단을 입력할까요? "))

    print("===== {}단 =====".format(x))
    
    for i in range(1, 10):
        print("{} X {} = {result}".format(x, i, result = x*i))

gugudan()