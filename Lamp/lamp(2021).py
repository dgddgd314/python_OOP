# 1번 : 생성자란?
# 생성자는 __init__ 처럼 정해져있는 함수의 이름 느낌.
class Lamp:
    STATECNT = 4
    
    def __init__(self):
        self.state = 0
        
    def switch_state(self):
        self.state = (self.state+1)% self.STATECNT # 2번 
        
    def set_state(self, new_state):
        if 0 <= new_state < self.STATECNT:
            self.state = new_state
        else:
            print(f"Invalid state {new_state}. State should be between 0 and {self.STATECNT - 1}.")
            
    def __str__(self):
        return f"Lamp state: {self.state}" # 3번 수정 부분
    
    # 4번: 기능 추가 구현

# 5번 : 상속 받는 코드
class MiniLamp(Lamp):
    def __init__(self):
        super().__init__() # 부모 클래스를 호출하는 느낌으로 생성.
        self.size = 10
        
    def __str__(self):
        return f"This includes function in Lamp. State is {self.state}, size is {self.size}."
    
"""
# 예시로 실행해볼 코드
lamp = Lamp()
print(lamp)

lamp.switch_state()
print(lamp)

minilamp = MiniLamp()
print(minilamp)

minilamp.switch_state()
print(minilamp)
"""


