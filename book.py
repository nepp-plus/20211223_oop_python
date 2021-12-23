# 책 한권을 나타내는 클래스 파일.

class Book:
    # 책을 구성하는 요소들 작성.
    
    # 책의 정보 세팅 기능. (제목, 대여료) => 함수(메쏘드) 작성.
    def set_data(self, title, rent_fee):
        # 지금 보려는 책(이 책)의 제목 / 대여료 설정.
        self.title = title
        self.rent_fee = rent_fee