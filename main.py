from urllib.request import urlopen

url = "https://news.ycombinator.com/e"

page = urlopen(url)
print(page)


html_bytes = page.read()
html = html_bytes.decode("utf-8")

print(html)