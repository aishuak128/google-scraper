import urllib
from requests.exceptions import RequestException
from requests_html import HTMLSession



class ParserGoogle():
    css_result = ".tF2Cxc"
    css_name = "h3"
    css_link = ".yuRUbf a"


    def __init__(self, keyword : str) -> None:
        self.keyword = keyword.lower()
        self.query = urllib.parse.quote_plus(keyword)        
        self.results = []


    def get_src_code(self, page : int=0):
        link = f'https://www.google.com/search?q={self.query}&start={page*10}'

        try:
            session = HTMLSession()
            response = session.get(link)
            return response
        except RequestException as e:
            print(e)
            raise e


    def parse_page(self, page : int=0):
        src = self.get_src_code(page)
        items = []
        css_name = self.css_name
        css_link = self.css_link
        css_result = self.css_result
        cards = src.html.find(css_result)

        if not cards: return items

        for card in cards:
            item = {
                'name': card.find(css_name, first=True).text,
                'link': card.find(css_link, first=True).attrs['href']
            }
            items.append(item)

        return items


