
from bs4 import BeautifulSoup
import re
import pymysql

class HtmlParser():

    def _get_new_urls(self, soup):
        new_urls = set()
        links = soup.find_all('a',href = re.compile('article/details'))

        for link in links:
            new_url = link['href']
            new_urls.add(new_url)
        return new_urls


    def _get_new_data(self, page_url, soup, count):
        new_datas = {}
        # <h6 class="title-article"></h6>
        if count != 1:
            # 获取标题，发表时间，阅读量，正文
            title_node = soup.find('title')

            time = soup.find(class_='time')

            read_count = soup.find(class_='read-count')
            article = soup.find('article')
            new_datas['title'] = title_node.get_text()
            new_datas['time'] = time.get_text()
            new_datas['read_count'] = read_count.get_text()
            new_datas['article'] = article.get_text()
            new_datas['url'] = page_url
            # 打开数据库连接
            db = pymysql.connect("localhost", "root", "123456", "tptest", use_unicode=True, charset="utf8")
            # 使用 cursor() 方法创建一个游标对象 cursor
            cursor = db.cursor()
            sql = "insert into spider(TITLE, TIME, READ_COUNT, URL)\
                   values('%s', '%s', '%s', '%s')" % ( new_datas['title'], new_datas['time'], new_datas['read_count'], new_datas['url'])
            try:
                # 执行sql语句
                cursor.execute(sql)
                # 提交到数据库执行
                db.commit()
            except:
                # 如果发生错误则回滚'
                db.rollback()
            finally:
                cursor.close()
                db.close()
        else:
            new_datas = None
        return new_datas

    def parser(self, page_url, html_cont, count):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parser')

        new_urls = self._get_new_urls(soup)

        new_data = self._get_new_data(page_url, soup, count)

        return new_urls, new_data
