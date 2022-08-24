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
    # clean_response = process_html(response)
    title: str = get_title(
        page=response.text
    )  # may want other info, this is a good proof of concept
    vid: dict = {
        url: title,
    }  # placeholder
    return vid


def main(filename: str) -> None:
    """
    main execution function
    """
    lines_from_file = simple_looper(filename=filename)
    for line in lines_from_file:
        print(line)
        this_vid: dict = get_info(url=line)
        print(this_vid)  # temp
        # do stuff with it here,
    # or here


if __name__ == "__main__":
    # I have too many youtube tabs-- for now, I manually saved their URLs to a local text file
    main(filename=c.YT_FILE)
