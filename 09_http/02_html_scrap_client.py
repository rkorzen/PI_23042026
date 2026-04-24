from html.parser import HTMLParser
from urllib.request import urlopen

HOST = "127.0.0.1"
PORT = 9003

class LinkParser(HTMLParser):

    def __init__(self):
        super().__init__()
        self.links = []
        self.current_href=""
        self.inside_link = False

    def handle_starttag(self, tag, attrs):
        if tag != "a":
            return
        self.inside_link = True
        self.current_href = dict(attrs).get("href", "")

    def handle_data(self, data):
        if self.inside_link and data.strip():
            self.links.append({"text": data.strip(), "href": self.current_href})

    def handle_endtag(self, tag):
        if tag == "a":
            self.inside_link = False
            self.current_href = ""

def main():

    url = f"http://{HOST}:{PORT}/"
    with urlopen(url) as response:
        html = response.read().decode("utf-8")
    parser = LinkParser()
    parser.feed(html)

    print("url:", url)
    for link in parser.links:
        print(f"{link['text']} -> {link['href']}")

if __name__ == "__main__":
    main()