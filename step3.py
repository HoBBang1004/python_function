
# 하단의 코드도 함수로 만들어보자

price = 10000
vat_rate = 0.1
print(price*vat_rate)


print('=======================')


def get_vat():
    price = 10000
    vat_rate = 0.1
    print(price*vat_rate)

get_vat() 


print('')
print('================= 응용 ====================')

# 위에 우리가 작성한 함수는 항상 값이 정해져 있어서 같은 값만 출력함 
# get_vat() 괄호에 우리가 원하는 숫자를 넣으면 그 숫자에 맞는 부가가치율을 계산할 수 있는 함수식 만들어보자


"""
 -> 이건 강사님이 작성하기 전에 내가 먼저 작성해본 코드
def get_vat2(num):
    price = num
    vat_rate = 0.1
    print(price*vat_rate)

"""

# 강사님 코드

"""
1. 가격만 변수로 설정하고 싶은 경우

def get_vat2(price):
    vat_rate = 0.1
    print(price*vat_rate)

get_vat2(100)
get_vat2(2000)

"""

"""
# 2. 가격과 비율 모두 변수로 설정하고 싶은 경우

def get_vat2(price,vat_rate):
    # vat_rate = 0.1
    print(price*vat_rate)

get_vat2(100, 100)
get_vat2(2000,0.2)

"""

"""
# 3. 만약 비율을 따로 작성하지 않았을 경우는 자동으로 0.1로 계산되게 하는 방법
def get_vat2(price,vat_rate=0.1):
    # vat_rate = 0.1
    print(price*vat_rate)

get_vat2(100)
get_vat2(2000,0.2)
"""


# 4. 위에 함수로 계산된 것을 값으로 표현하고 싶다면?
# return을 작성하면 됨 


def get_vat2(price,vat_rate=0.1):
  
    return price*vat_rate


print(get_vat2(10000))
print(get_vat2(2000,0.2))

# 만약에 이메일을 보내는 함수도 만든다면 하단의 코드를 입력했을 때 이메일도 보낼 수 있다고 함 
# email.send('dbwjd0@naver.com', get_vat2(10000,0.3)) -> 물론 지금은 동작하지 않음




print('')
print('================= 응용2 ====================')

# 여긴 그냥 내가 해보는 것
# 사용자에게 가격과 비율의 입력받아서 동적으로 계산하는 함수 

price = int(input('price? (only int형만 가능) : '))
vat_rate = input('vat_rate? : ')


def get_vat3(price,vat_rate):
    return price*float(vat_rate)

print(get_vat3(price,vat_rate))

"""
    * 주의할 점 이때 그냥 input이라고 하면 string형이기 때문에 
      int(input())이라고 해야 int형이됨 

      만약 입력받은 price(vat_rate)를 int(float)형으로 입력요청할 경우 혹은 
      함수를 정의할 땨 형변환하지 않으면 실행할 때 오류 발생함!!

      ==> 즉, 형변환 필수!!


"""
