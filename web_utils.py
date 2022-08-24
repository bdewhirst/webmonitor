from bs4 import BeautifulSoup

# this header gets 'please update your browser' on youtube
# HEADERS: dict = {
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
#     "Pragma": "no-cache",
#     "Cache-Control": "no-cache",
# }

BASIC_HEADERS: dict = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache",
}

HEADERS: dict = {
    "User-Agent": "Custom user agent",
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


def get_title(page: str) -> str:
    """
    Get everything in the title tag (<title>...</title>) and return it as a string
    """
    soup = BeautifulSoup(page, "html.parser")
    title = soup.find("title")
    title_ = title.string
    return title_
