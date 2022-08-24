import requests

import local_constants as c
from web_utils import process_html, get_title, HEADERS


def simple_looper(filename: str) -> list:
    """
    Given a string specifying a local filename's location, return a list of rows in that file
    """
    all_data: list = []

    try:
        with open(filename, "r") as f:
            for line in f:
                # print(line)
                all_data.append(line)
        return all_data
    except IOError:
        msg = "something went wrong"


def get_info(url: str) -> dict:
    """
    For a given url (represented as a string), get relevant youtube data and return results as a dict with url as key
    """
    response = requests.get(url, headers=HEADERS)
    processed_response: str = process_html(response.text)
    # processed_response has useful information-- just get the title (between <title> and </title>


    stuff = []  # placeholder
    vid: dict = {url: stuff}
    return vid


def main(filename: str) -> None:
    """
    main execution function
    """
    lines_from_file = simple_looper(filename=filename)
    for line in lines_from_file:
        print(line)
        get_info(url=line)


if __name__ == "__main__":
    # I have too many youtube tabs-- for now, I manually saved their URLs to a local text file
    main(filename=c.YT_FILE)
