import urllib.request

class HtmlDownloader():

    def download(self, url):
        if url is None:
            return None
        request = urllib.request.Request(url)
        response = urllib.request.urlopen(request)
        if response.getcode() != 200:
            return None
        buff = response.read().decode("utf8")
        return buff