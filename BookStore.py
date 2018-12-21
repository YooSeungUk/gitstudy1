class BookStore:  ## 서점 클래스

    def __init__(self):  ## 서점 클래스를 만들면 서점은 books라는 리스트를 가진다
        self.books = []
        
    def add(self, book):    ## add 함수는 서점 클래스에 있는 books 리스트에 책을 넣는다 (책은 가격과 포인트를 가진 클래스)
        self.books.append(book)
    
    
    def min_price(self): ## 가장 가격이 낮은 값을 계산해주는 함수

        for i in range(0, len(self.books)-1): ## 서점의 책들을 포인트 순으로 정렬해준다 포인트가 크면 앞으로 낮은거는 뒤로 간다
                                                ## 삽입 정렬이며 가격이 크면 앞으로 작으면 뒤로 보낸다
            for j in range(i+1,len(self.books)):  
                 
                    if self.books[i].point < self.books[j].point:
                        temp = self.books[i]
                        self.books[i] = self.books[j] 
                        self.books[j] = temp
        

        
        min_pay = self.books[0].price  ## 맨 앞에 있는 책의 가격과 포인트를 변수에 넣어준다 이것은 계속 사용 예정
        remain_point = self.books[0].point 
        
        for i in range(1, len(self.books)): ## book 변수에 첫번쨰 책을 넣는다
            book = self.books[i]
            if book.price >= remain_point:  ##만약 첫번째 책의 가격이 포인트보다 많이 남아있다면  
                min_pay = min_pay + book.price - remain_point ##책의 가격을 모아놓은 변수와 현재책의 가격을 더하고 포인트를 빼준다
         
                remain_point = book.point  ##그리고 책을 샀으니 책의 포인트는 남아있는 포인트변수에 넣는다
            else:
                remain_point = remain_point - book.price + book.point ## 포인트가 사려고 하는 책의 가격보다 높을떄
        
        return min_pay
        

