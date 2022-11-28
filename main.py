
from parser_google import ParserGoogle
from db_conn import cursor, conn


keywords = ('Sports', 'Lottery', 'slot', 'casino', 'sports lottery India', 'Horse Racing bet')


for keyword in keywords:
    page_n = 0
    parser = ParserGoogle(keyword)

    while True:
        parsed = parser.parse_page(page_n)
        print(f'{parsed=}')
        if not parsed: break

        for data in parsed:
            cursor.execute("INSERT INTO google_search_results (title, link, keyword) VALUES (%s, %s, %s)", (data['name'], data['link'], parser.keyword))

        print(f'{keyword=}', f'{page_n=}')
        conn.commit()
        page_n += 1
        

    