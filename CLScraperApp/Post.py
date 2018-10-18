from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import URLError
import re


class Post(object) :
    
    def __init__(self, post_id, locale, location, category, post_title, photos='', url='', title='', content='', status = 0, details='', price=''):
        
        self.post_id = post_id
        self.url = ('https://{}.craigslist.org/{}/d/{}/{}.html').format(locale, category, post_title, post_id)
        self.location = location
        self.locale = locale
        self.category = category
        self.title = title
        self.post_title = post_title
        self.content = content
        self.status = status
        self.photos = photos
        self.details = details
        self.price = price
        
        self.get_post()

    def get_post(self):

        try:
            soup = BeautifulSoup(urlopen(self.url).read(), "lxml")

            post_content = str(soup.find(id='postingbody'))
            post_content = re.sub(r'(QR Code Link to This Post)','', post_content, flags=re.IGNORECASE)
            self.content = post_content

            post_photos = soup.find_all('figure')
            for post_photo in post_photos:
                post_photo.get('class')
            self.photos = post_photos

            post_details = soup.find_all('p', class_='attrgroup')
            self.details = post_details

            post_price = soup.find_all('span', class_='price')
            self.price = post_price

        except URLError as error:
            pass

    def get_location(self):
        return self.location

    def get_locale(self):
        return self.locale

    def get_category(self):
        return self.category

    def get_title(self):
        try: 
            soup = BeautifulSoup(urlopen(self.url).read(), "lxml")
            self.title = soup.title.string

            title_string = str(soup.title.string)
            title_string = re.sub(r'\ - cars & trucks - by owner - vehicle automotive sale','', title_string, flags=re.IGNORECASE)

            self.post_title = title_string

        except URLError as error:
            pass

    def get_post_title(self):
        return self.post_title

    def get_body(self):
        return self.content

    def get_photos(self):
        return self.photos

    def get_price(self):
        return self.price

    def get_details(self):
        return self.details

    def get_url(self):
        return self.url

    def __str__(self):
        return 'Title:{title}. Locale:{locale}. Location:{location}. Category:{category}'\
            .format(title= self.title, locale=self.locale, location= self.location, category= self.category)
