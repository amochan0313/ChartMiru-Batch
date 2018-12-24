import json
from typing import List, Dict

import pandas

from monogoto import app
from monogoto.articles import Articles
from monogoto.models.blog import Blog
from monogoto.models.static_dictionary import StaticDictionary
from monogoto.words import Words


class Csv():
    @staticmethod
    def convert_csv_array() -> array:
        initial_blogs = []
        df = pandas.read_csv(app.root_path + '/' + app.config['INITIAL_BLOGS_PATH'])
        for index, row in df.iterrows():
            blog = Blog.get_blog(url=row['url'])
            if len(blog) <= 0:
                continue

            initial_blogs.append({
                'id': blog['id'],
                'type': row['type'],
                'title': blog['title'],
                'blog_url': row['url'],
                'scraping_xpath': blog['scraping_xpath']
            })

        return initial_blogs

    @staticmethod
    def create_test_data(input_path: str, output_path: str) -> None:
        # json読み込み
        f = open(input_path, 'r')
        data = json.load(f)
        f.close()

        results = []

        # words抜き出し
        for i in range(len(data)):
            blog = data[i]
            scraped = Articles.scrape_article(blog['url'])
            w = Words()
            words = w.get_noun(scraped['content'], StaticDictionary.DICTIONARY_IGNORE_ML_WORDS)
            results.append([
                blog['url'],
                words,
                blog['category_id']
            ])
            app.logger.info('Scraped:[%d/%d]' % (i + 1, len(data)))

        # csv書き出し
        df = pandas.DataFrame(results, columns=["url", "words", "category_id"])
        df.to_csv(output_path)
