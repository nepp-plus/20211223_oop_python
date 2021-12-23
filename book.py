# 책 한권을 나타내는 클래스 파일.

class Book:
    # 책을 구성하는 요소들 작성.
    
    # 책의 정보 세팅 기능. (제목, 대여료) => 함수(메쏘드) 작성.
    def set_data(self, title, rent_fee):
        # 지금 보려는 책(이 책)의 제목 / 대여료 설정.
        
        # self.아무변수나생성  = 초기값대입
        self.book_title = title
        self.book_rent_fee = rent_fee
        
        # self.에서 만든 변수들만 생성된 변수임. => 가져다 쓸때도, self.변수명에 유의해서 사용해야함.