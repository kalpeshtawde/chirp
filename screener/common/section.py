import logging
import pandas as pd
from datetime import datetime

from screener.models import Company, Results, BalanceSheet, Shareholding, \
    Ratios, CashFlow

pd.options.plotting.backend = "plotly"

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)


class Section:
    def __init__(self):
        self.function_map = {
            'quarters': self.process_quarters,
            'balance-sheet': self.process_balance_sheet,
            'cash-flow': self.process_cash_flow,
            'ratios': self.process_ratios,
            'shareholding': self.process_shareholding,
        }

    def process(self, section_id, data, index, columns):
        if section_id in self.function_map:
            df = pd.DataFrame(
                data,
                index=index,
                columns=columns
            ).replace("", None)
            company = Company.objects.all().first()
            self.function_map[section_id](df, company)
        else:
            log.warning(f"No mapping for section {section_id}")

    def process_cash_flow(self, df, company):
        for idx, col in df.iteritems():
            cash_flow = CashFlow(
                company=company,
                date=datetime.strftime(
                    datetime.strptime(col.name, '%b %Y'), '%Y-%m-%d'
                ),
                operating=col["Cash from Operating Activity"],
                investing=col["Cash from Investing Activity"],
                financing=col["Cash from Financing Activity"],
                net=col["Net Cash Flow"],
            )
            cash_flow.save()

    def process_ratios(self, df, company):
        for idx, col in df.iteritems():
            ratios = Ratios(
                company=company,
                date=datetime.strftime(
                    datetime.strptime(col.name, '%b %Y'), '%Y-%m-%d'
                ),
                debtor_days=col["Debtor Days"],
                inventory_days=col["Inventory Days"],
                days_payable=col["Days Payable"],
                cash_conversion_cycle=col["Cash Conversion Cycle"],
                working_capital_days=col["Working Capital Days"],
                roce_pct=col["ROCE"],
            )
            ratios.save()

    def process_shareholding(self, df, company):
        for idx, col in df.iteritems():
            cash_flow = Shareholding(
                company=company,
                date=datetime.strftime(
                    datetime.strptime(col.name, '%b %Y'), '%Y-%m-%d'
                ),
                promoters_pct=col["Promoters"],
                fii_pct=col["FIIs"],
                dii_pct=col["DIIs"],
                government_pct=col["Government"],
                public_pct=col["Public"],
            )
            cash_flow.save()

    def process_balance_sheet(self, df, company):
        for idx, col in df.iteritems():
            bs = BalanceSheet(
                company=company,
                date=datetime.strftime(
                    datetime.strptime(col.name, '%b %Y'), '%Y-%m-%d'
                ),
                share_capital=col["Share Capital"],
                reserves=col["Reserves"],
                borrowings=col["Borrowings"],
                other_liabilities=col["Other Liabilities"],
                total_liabilities=col["Total Liabilities"],
                fixed_assets=col["Fixed Assets"],
                cwip=col["CWIP"],
                investments=col["Investments"],
                other_assets=col["Other Assets"],
                total_assets=col["Total Assets"],
                unit="CR",
            )
            bs.save()

    def process_quarters(self, df, company):
        for idx, col in df.iteritems():
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
