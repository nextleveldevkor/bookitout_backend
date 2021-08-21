# BookItOut

검색을 통해 도서관의 대출 현황과 판매자가 등록해놓은 중고 도서를 확인할 수 있습니다.

## How to run

```
git clone https://github.com/nextleveldevkor/bookitout_backend.git

pip3 install -r requirements.txt

python3 manage.py runserver
or
python manage.py runserver
```

```
기능 설명

# libraries
libraries/ : [POST] {search_title} -> {title, author, link, img_link, available_num}

libraries/status : [POST] {link} -> {library status of a book}

#service
products/ : [GET] -> 최근 등록한 매물 순
products/search & parameter : [GET] -> 검색어에 대한 책 목록 및 매물 등록 개수
products/search/details & parameter: [GET] -> 해당 책에 대한 매물 상세 정보 및 최저 가격순 정렬
```
