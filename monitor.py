import os
import time
import logging
import winsound

import requests

# from twilio.rest import Client
# import yagmail

from web_utils import process_html, BASIC_HEADERS


import local_constants as c


# def send_email_alert(alert_str):
#     """Sends an email alert. The subject and body will be the same."""
#     yagmail.SMTP(c.SENDING_EMAIL_USERNAME, c.SENDING_EMAIL_PASSWORD).send(
#         c.RECIPIENT_EMAIL_ADDRESS, alert_str, alert_str
#     )


# def send_text_alert(alert_str):
#     """Sends an SMS text alert."""
#     client = Client(c.TWILIO_ACCOUNT_SID, c.TWILIO_AUTH_TOKEN)
#     message = client.messages.create(
#         to=c.TWILIO_PHONE_RECIPIENT, from_=c.TWILIO_PHONE_SENDER, body=alert_str
#     )


def do_beep():
    """make several 'beep' noises, assuming a PyCharm framework"""
    winsound.Beep(frequency=700, duration=2000)


def first_page_cache(filename: str, contents: str) -> None:
    """Save the initial state of the web page to be monitored"""
    text_file = open(filename, "w+", encoding="utf-8")
    text_file.write(contents)
    text_file.close()


def webpage_was_changed(filename: str):
    """Returns true if the webpage was changed, otherwise false."""
    response = requests.get(c.URL_TO_MONITOR, headers=BASIC_HEADERS)
    processed_response_html = process_html(response.text)

    # create the text file specified by filename, which will store the initial state of the page
    if not os.path.exists(filename):
        first_page_cache(filename=filename, contents=processed_response_html)

    filehandle = open(filename, "r", encoding="utf-8")
    previous_response_html = filehandle.read()
    filehandle.close()

    is_same = processed_response_html == previous_response_html
    return not is_same


def main(filename: str):
    log = logging.getLogger(__name__)
    logging.basicConfig(
        level=os.environ.get("LOGLEVEL", "INFO"), format="%(asctime)s %(message)s"
    )
    log.info("Running Website Monitor")

    if os.path.exists(filename):
        os.remove(filename)
        log.info("file deleted for initialization")

    while True:
        try:
            if webpage_was_changed(filename=filename):
                log.info("WEBPAGE WAS CHANGED.")
                do_beep()
                # send_text_alert(f"URGENT! {c.URL_TO_MONITOR} WAS CHANGED!")
                # send_email_alert(f"URGENT! {c.URL_TO_MONITOR} WAS CHANGED!")
                return None
            else:
                log.info("Webpage was not changed.")
        except:
            log.info("Error checking website.")
        time.sleep(c.DELAY_TIME)


if __name__ == "__main__":
    main(filename=c.FILENAME)
