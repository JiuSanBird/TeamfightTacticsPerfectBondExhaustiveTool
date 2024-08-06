import urllib.request
import urllib.parse  # 解析器
from bs4 import BeautifulSoup


def ask_url(url):
    # 用headers可以让网站觉得我们是个浏览器
    # 用户代理：告诉浏览器，我们可以接受什么水平的文件内容
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3776.400 QQBrowser/10.6.4212.400 "}
    # 请求对象（封装）
    request = urllib.request.Request(url=url, headers=headers, method="GET")
    # 发送请求并获取响应内容
    response = urllib.request.urlopen(request)
    html = response.read().decode('utf-8')
    # 使用 BeautifulSoup 解析 HTML
    html = BeautifulSoup(html, "html.parser")
    html = html.encode('utf-8').decode('unicode_escape')  # 版本答案

    return html
