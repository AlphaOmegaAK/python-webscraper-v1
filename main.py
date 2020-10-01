from urllib.request import urlopen

url = "https://news.ycombinator.com//"

page = urlopen(url)
# print(page)


html_bytes = page.read()
html = html_bytes.decode("utf-8")

# print(html)

title_index = html.find('<title>')

# print(title_index)


start_index = title_index + len("<title>")

# print(start_index)

end_index = html.find("</title>")

title = html[start_index:end_index]
print(title)
