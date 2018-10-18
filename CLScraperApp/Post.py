from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import URLError
import re
from datetime import datetime, timedelta


class Post(object) :
    
    def __init__(self, post_id, locale, location, category, post_title, url='', title='', content='', email='', date='', status = 0):
        
        self.post_id = post_id
        self.url = ('https://{}.craigslist.org/{}/d/{}/{}.html').format(locale, category, post_title, post_id)
        self.location = location
        self.locale = locale
        self.category = category
        self.title = title
        self.post_title = post_title
        self.content = content
        self.email = email
        self.date = date
        self.status = status
        
        self.get_post()

    def get_post(self):

        try:
            soup = BeautifulSoup(urlopen(self.url).read(), "lxml")

            post_content = str(soup.find(id='postingbody'))
            post_content = re.sub(r'(QR Code Link to This Post)','', post_content, flags=re.IGNORECASE)

            self.content = post_content

            for reply in soup.find_all('a', {'id':'replylink'}):
                if reply is not None :
                    reply_link = reply["href"]
                    reply_url = self.url[:self.url.find('.org') + 4] + reply_link
                    reply_page = BeautifulSoup(urlopen(reply_url).read())
                    self.email = reply_page.find('p', class_='anonemail')

        except URLError as error:
            pass

    def get_location(self):
        return self.location

    def get_locale(self):
        return self.locale

    def get_category(self):
        return self.category

    def get_category_full_name(self):
        return self.category_full_name

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

    def get_email(self):
        return self.email

    def get_date(self):
        return self.date

    def get_url(self):
        return self.url

    def __str__(self):
        return 'Title:{title}. Date:{date}. Email:{email}. Location:{location}. Locale:{locale}. Category:{category}'\
            .format(title= self.title, date= self.date, email= self.email, locale=self.locale, location= self.location, category= self.category)
