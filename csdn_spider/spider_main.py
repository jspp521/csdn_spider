
from csdn_spider import url_manager
from csdn_spider import html_downloader
from csdn_spider import html_outputer
from csdn_spider import html_parser

class SpiderMain():
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutPuter()

    def craw(self,root_url):
        count = 1

        self.urls.add_new_url(root_url)

        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()

                print('craw %d : %s' % (count,new_url))
                html_cont = self.downloader.download(new_url)

                new_urls, new_data = self.parser.parser(new_url, html_cont, count)

                self.urls.add_new_urls(new_urls)
                # self.outputer.collect_data(new_data)
                # 只获取100条
                if count == 101:
                    break
                count += 1
            except:
                print('craw %d 失败' % count)

        self.outputer.output_html()


if __name__=="__main__":
    root_url = "https://www.csdn.net/"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)