import turtle as tur
import colorsys as cs

tur.setup(800, 800)      # 창 크기
tur.bgcolor('black')     # 검은 배경이라 색이 더 선명해 보임
tur.title('Rainbow Flower')
tur.hideturtle()         # 거북이 모양 숨기기
tur.speed(0)             # 가장 빠르게
tur.tracer(3)            # 3번 그릴 때마다 한 번씩 화면 갱신 (너무 느리면 숫자를 키우기)
tur.width(1.5)

PETALS = 18      # 꽃잎 개수 (360 / 18 = 20도 간격)
LINES = 16       # 꽃잎 하나를 이루는 선 개수
CENTER = 45      # 가운데 검은 구멍의 반지름
BIG = 260        # 가장 바깥 꽃잎 선의 반지름
TWIST = 18       # 꽃잎을 살짝 비틀어서 소용돌이 느낌 내기

# 꽃잎 모양 하나 그리기:
# 60도짜리 원호 → 120도 왼쪽으로 꺾기 → 60도짜리 원호 → 120도 꺾기
# = 양 끝이 뾰족한 나뭇잎 모양, 그리고 나면 처음 자리·방향으로 돌아옴
def leaf(r):
    tur.circle(r, 60)
    tur.left(120)
    tur.circle(r, 60)
    tur.left(120)

for k in range(PETALS):
    angle = k * 360 / PETALS          # 이 꽃잎이 뻗어 나갈 방향

    # 가운데 구멍 가장자리로 이동 (펜 들고)
    tur.penup()
    tur.goto(0, 0)
    tur.setheading(angle)
    tur.forward(CENTER)
    # leaf()는 시작 방향보다 30도 왼쪽으로 뻗으니까 30을 빼서 맞추고, TWIST만큼 비틂
    tur.setheading(angle - 30 + TWIST)
    tur.pendown()

    hue = k / PETALS                  # 꽃잎마다 색상(무지개 순서)
    for j in range(LINES):
        r = BIG - j * (BIG - 30) / LINES          # 바깥 → 안쪽으로 점점 작은 꽃잎
        sat = j / (LINES - 1)                     # 바깥은 흰색(채도 0) → 안쪽은 진한 색(채도 1)
        tur.pencolor(cs.hsv_to_rgb(hue, sat, 1))  # HSV → RGB(0~1)로 바꿔서 펜 색 지정
        leaf(r)

# 가운데 동그라미 테두리
tur.penup()
tur.goto(0, -CENTER + 8)
tur.setheading(0)
tur.pendown()
tur.pencolor('white')
tur.circle(CENTER - 8)

tur.update()     # tracer 때문에 남은 부분까지 화면에 그리기
tur.done()       # 창이 바로 닫히지 않게
