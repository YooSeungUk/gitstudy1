class Book:
    price = 0
    point= 0
    def __init__(self, price, point): ##생성자로서 가격과 포인트가 파라미터로 주어지면 이 클래스의 가격과 포인트가 갱신된다.
        self.price = price
        self.point =point

