import re
import requests
import logging
from bs4 import BeautifulSoup

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)


class Screener:

    def __init__(self):
        self.data = {}

    def get_top_ratios(self, soup):
        data = {}
        top_ratios_ul = soup.find("ul", id="top-ratios")
        top_ratios_li = top_ratios_ul.find_all("li")
        for t in top_ratios_li:
            text = t.get_text()
            text = re.sub(r" |₹|Cr.|%|,", "", text)
            text = re.sub(r"\n", " ", text)
            text = text.strip().split(" ")
            data[text[0]] = text[-1]
        self.data["top_ratios"] = data

    def get_section(self, soup, section_id):
        try:
            quarters_section = soup.find("section", id=section_id)
            quarters_table = quarters_section.find(
                "table", {"class": "data-table"})
            quarters_tr = quarters_table.find_all("tr")
            for tr in quarters_tr:
                tds = tr.find_all(lambda tag: tag.name=="td" or tag.name=="th")
                for td in tds:
                    text = td.get_text()
                    text = re.sub(r"₹|Cr.|%|,", "", text)
                    text = text.strip()
                    print(text)
        except Exception as error:
            log.error(
                f"Parsing failed for section {section_id} with error {error}"
            )

    def get_mainpage(self, url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                return soup
            else:
                log.error(f"Download mainpage for {url} failed")
        except Exception as error:
            log.error(f"Download mainpage for {url} failed with error {error}")


obj = Screener()
soup = obj.get_mainpage("https://www.screener.in/company/TATAPOWER/")
obj.get_top_ratios(soup)
obj.get_section(soup, "quarters")
obj.get_section(soup, "profit-loss")
obj.get_section(soup, "balance-sheet")
obj.get_section(soup, "cash-flow")
obj.get_section(soup, "ratios")
obj.get_section(soup, "shareholding")
