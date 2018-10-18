from __future__ import print_function
from datetime import datetime
from urllib.error import URLError
from urllib.request import urlopen
import re
from bs4 import BeautifulSoup

from Post import Post


def get_globals():
    try:
        config = {}
        exec (open('config.conf').read(), config)
        locales = config['locales']
        categories = config['categories']
        query_strings = config['query_strings']
        return locales, categories, query_strings
    except Exception as e:
        raise


def get_posts(locale, category, query_string):
    posts = []

    url = ('https://' + locale + '.craigslist.org/search/' + category + '?' + query_string)
    try:
        soup = BeautifulSoup(urlopen(url).read(), "lxml")
    except URLError:
        raise

    links = []

    for link in soup.find_all(class_='result-title hdrlnk'):
        print(link.get('href'))
        links.append(link.get('href'))

        # example -- https://lincoln.craigslist.org/cto/d/2014-toyota-tacoma-4x4-double/6712707059.html
    for link in links:
        temp = link.split("/")
        location = temp[2].replace(".craigslist.org", "")
        post_title = temp[5]
        post_id = temp[6].replace(".html", "")
        posts.append(Post(post_id, location, locale, category, post_title))

    return posts


def make_html(locales, categories, posts):
    # http://jinja.pocoo.org/docs/2.10/
    from jinja2 import Environment, PackageLoader
    env = Environment(loader=PackageLoader('scraper', 'template'))
    template = env.get_template('template.html')
    html_output = template.render(locales=locales, categories=categories, posts=posts)
    output_destination = '{}.html'.format(datetime.now().strftime('%Y%m%d%H%M'))

    with open(output_destination, 'wb') as output:
        output.write(bytes(html_output, 'UTF-8'))


def main():
    locales, categories, query_strings = get_globals()
    posts = []

    for locale in locales:
        for category in categories:
            for query_string in query_strings:
                posts.extend(get_posts(locale, category, query_string))

    make_html(locales, categories, posts)
    print('Posts found:{n_posts}. Done!'.format(n_posts=len(posts)))


if __name__ == '__main__':
    main()
