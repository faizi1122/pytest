from selenium.webdriver.support.wait import WebDriverWait

from .common.BasePage import BasePage
from utilities.conftest import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

from mailosaur import MailosaurClient
from mailosaur.models import SearchCriteria

from datetime import datetime, timedelta


class CommonFunctions(BasePage):

    def go_to_forgot_password_screen(self):
        pass

    def go_to_forgot_password_details(self):
        pass

    def get_email_response(self):

        # Available in the API of a server
        api_key = get_config("KEYS", "api_key")
        server_id = get_config("KEYS", "server_id")
        server_domain = get_config("KEYS", "server_domain")

        mailosaur = MailosaurClient(api_key)

        criteria = SearchCriteria()

        # criteria.sent_to = "arrive-satellites@" + server_domain
        criteria.sent_from = "contact-us@skinfitness.com.sg"
        expected_email_subject = ""
        if get_config("URL", "url") == "https://ci.tst.sq.servicequik.com":
            expected_email_subject = "Invoice from SkinFitness"
        elif get_config("URL", "url") ==  "https://curry.preprod-01.ap-southeast-1.servicequik.net":
            expected_email_subject = "Invoice from Curry Food Services"
            criteria.sent_from = "admin@servicequik.com"
        else:
            expected_email_subject = "Invoice from automated-testing"
        criteria.subject = expected_email_subject
        # Search for all messages sent to someone@SERVER_ID.mailosaur.net,
        # received in the last 2 hours. Limit results to the first 10 matches only.
        two_minutes_ago = datetime.today() - timedelta(minutes=2)
        try:
            email = mailosaur.messages.get(server_id, criteria, received_after=two_minutes_ago, timeout=60000)
        except:
            assert False, "Exception (Timeout 1 minute): The invoice email is not received."
        link = email.html.links[0]
        print("Mailosaur link: " + link.href)
        link = link.href
        return link
