from Book import Book
from BookStore import BookStore


case =0
test_case = int(input()) ## 테스트케이스를 받는다.
while case<test_case: ## 테스크케이스만큼 반복한다
    book = input()  ##책의 수와 서점 수를 입력받는다
    book_number = int(book[0])
    book_store_number = int(book[2])


    Book_Store = [0]*book_store_number ## 서점 수만큼의 배열을 만든다

    for i in range(0,book_store_number): ## 만든 배열에 서점 클래스(객체)를 넣어준다
        Book_Store[i] = BookStore()
    i = 0 ##반복변수
    while i<book_number: # 책 수만큼 반복
        in_put = input() ## 책 가격과 포인트 입력
        in_put= in_put.strip() ## 양끝 공백제거
        in_put=in_put.split(" ") ## 문자열 사이에 공백제거

        for j in range(0, book_store_number*2, 2): ##책의 가격과 포인트를 각각 서점에 넣어줄 for문
            price = int(in_put[j]) ## price에는 책의 가격  j는 0,2,4 가격이 0,2,4줄에 있기때
            point = int(in_put[j+1]) ## point에는 책의 포인트가 들어간다 j+1는 1,3,5 포인트가 1,3,5줄에 있기때
            price_point = Book(price, point) ## 위에 break가 발동안됬을시 가격과 포인트로 Book 객체를 만든다
            Book_Store[int(j/2)].add(price_point) ## while문 위에 만든 서점 배열에 차곡차곡 책을 더해 넣는다
        i= i +1 ## 반복변수 +1

    pay = Book_Store[0].min_price()  ## pay 변수에 첫번쨰 서점의 가장 싼 가격 넣기
    for i in range(1, book_store_number):  ## 나머지 서점가격 게산을 위한 for문
        if pay>Book_Store[i].min_price(): ## 만약 pay보다 다른 서점의 값이 더 싸다면 pay에 그 값을 넣어줌
            pay = Book_Store[i].min_price()

    print(pay) ## 가격 출력

