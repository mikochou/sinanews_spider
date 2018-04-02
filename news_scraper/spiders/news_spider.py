import scrapy
import pprint


class SinaSpider(scrapy.Spider):
    name = "sina"

    def start_requests(self):
        """
        发出 http requests，对于 response 调用处理函数
        """
        urls = [
            'https://www.sina.com.cn/',  # 新浪首页
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        """
        解析 http 协议返回的 response，解析网页中的标题信息，结果输出到屏幕
        Args:
          response: scrapy.http.response.html.HtmlResponse 对象
        """
        match = ['//li/a', '//h2/a', '//h3/a']  # 常见包含文本的html标签前缀
        suffix = ['html', 'shtml', 'htm']  # 常见网页后缀
        # 解析，获取标题及其对应的url
        data = [urls.xpath("text()""|@href").extract() for i in match
                for urls in response.xpath(i)]
        # 过滤，得到结果
        titles = [i[1] for s in suffix for i in data
                  if len(i) == 2 and len(i[1]) > 9 and s in i[0].split('.')]
        # 结果输出到屏幕
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(titles)
