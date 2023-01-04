import re
import requests
import logging
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime

from django.core.management.base import BaseCommand

from screener.models import Company, Results


pd.options.plotting.backend = "plotly"

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

    def process_quarters(self, data, index, columns):
        df = pd.DataFrame(
            data,
            index=index,
            columns=columns
        )
        company = Company.objects.all().first()
        for idx, col in df.iteritems():
            print(col["Operating Profit"])
            results = Results(
                company=company,
                date=datetime.strftime(
                    datetime.strptime(col.name, '%b %Y'), '%Y-%m-%d'
                ),
                sales=col["Sales"],
                expenses=col["Expenses"],
                operating_profit=col["Operating Profit"],
                opm=col["OPM"],
                other_income=col["Other Income"],
                interest=col["Interest"],
                depreciation=col["Depreciation"],
                profit_before_tax=col["Profit before tax"],
                tax=col["Tax"],
                net_profit=col["Net Profit"],
                eps=col["EPS in Rs"],
                unit="CR",
            )
            results.save()

    def process_section(self, soup, section_id):
        try:
            index = []
            columns = []
            data = []

            quarters_section = soup.find("section", id=section_id)
            quarters_table = quarters_section.find(
                "table", {"class": "data-table"})
            quarters_tr = quarters_table.find_all("tr")
            for tr in quarters_tr:
                row = []
                start = True
                tds = tr.find_all(lambda tag: tag.name in ["td", "th"])
                for td in tds:
                    text = td.get_text()
                    text = re.sub(r"₹|Cr.|%|,|\xa0\+", "", text)
                    text = text.strip()

                    if td.name == "th":
                        if text:
                            columns.append(text)
                    elif start and text:
                        index.append(text)
                        start = False
                    else:
                        row.append(text)
                if row:
                    data.append(row)

            if data:
                self.process_quarters(data, index, columns)
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


class Command(BaseCommand):

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **option):
        obj = Screener()
        soup_obj = obj.get_mainpage(
            "https://www.screener.in/company/TATAPOWER/consolidated/"
        )
        obj.get_top_ratios(soup_obj)
        obj.process_section(soup_obj, "quarters")
        # obj.process_section(soup, "profit-loss")
        # obj.process_section(soup, "balance-sheet")
        # obj.process_section(soup, "cash-flow")
        # obj.process_section(soup, "ratios")
        # obj.process_section(soup, "shareholding")
