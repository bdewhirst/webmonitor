from bs4 import BeautifulSoup


HEADERS: dict = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache",
}


def process_html(string):
    soup = BeautifulSoup(string, features="lxml")

    # make the html look good
    soup.prettify()

    # remove script tags
    for s in soup.select("script"):
        s.extract()

    # remove meta tags
    for s in soup.select("meta"):
        s.extract()

    # convert to a string, remove '\r', and return
    return str(soup).replace("\r", "")
