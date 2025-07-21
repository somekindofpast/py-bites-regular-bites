"""Tax Bracket Calculator

Here is the break-down on how much a US citizen's income was
taxed in 2019

      $0 - $9,700   10%
  $9,701 - $39,475  12%
 $39,476 - $84,200  22%
 $84,201 - $160,725 24%
$160,726 - $204,100 32%
$204,101 - $510,300 35%
$510,301 +          37%

For example someone earning $40,000 would
pay $4,658.50, not $40,000 x 22% = $8,800!

    9,700.00 x 0.10 =       970.00
   29,775.00 x 0.12 =     3,573.00
      525.00 x 0.22 =       115.50
----------------------------------
              Total =     4,658.50

More detail can be found here:
https://www.nerdwallet.com/blog/taxes/federal-income-tax-brackets/

Sample output from running the code in the if/main clause:

          Summary Report
==================================
 Taxable Income:        40,000.00
     Taxes Owed:         4,658.50
       Tax Rate:           11.65%

         Taxes Breakdown
==================================
    9,700.00 x 0.10 =       970.00
   29,775.00 x 0.12 =     3,573.00
      525.00 x 0.22 =       115.50
----------------------------------
              Total =     4,658.50
"""
from dataclasses import dataclass, field
from typing import List, NamedTuple, Optional

Bracket = NamedTuple("Bracket", [("end", int), ("rate", float)])
Taxed = NamedTuple("Taxed", [("amount", float), ("rate", float), ("tax", float)])
BRACKET = [
    Bracket(9_700, 0.1),
    Bracket(39_475, 0.12),
    Bracket(84_200, 0.22),
    Bracket(160_725, 0.24),
    Bracket(204_100, 0.32),
    Bracket(510_300, 0.35),
    Bracket(510_301, 0.37),
]

@dataclass
class Taxes:
    """Taxes class

    Given a taxable income and optional tax bracket, it will
    calculate how much taxes are owed to Uncle Sam.

    """
    income: int
    tax_bracket: Optional[list[Bracket]] = None
    tax_amounts: list[Taxed] = None

    def __init__(self, income: int, tax_bracket=None):
        self.income = income
        if tax_bracket is None:
            self.tax_bracket = BRACKET
        else:
            self.tax_bracket = tax_bracket

    def __str__(self) -> str:
        """Summary Report

        Returns:
            str -- Summary report

            Example:

                      Summary Report
            ==================================
             Taxable Income:        40,000.00
                 Taxes Owed:         4,658.50
                   Tax Rate:           11.65%
        """
        taxes_total = self.taxes
        res = "          Summary Report          \n"
        res += "==================================\n"
        res += f"Taxable Income:        {self.income:,.2f}\n"
        res += f"Taxes Owed:         {taxes_total:,.2f}\n"
        res += f"Tax Rate:           {self.tax_rate:.2f}%"
        return res

    def report(self):
        """Prints taxes breakdown report"""
        print(self)
        print("\n         Taxes Breakdown          ")
        print("==================================")
        for tax_amount in self.tax_amounts:
            print(f"{tax_amount.amount:,.2f} x {tax_amount.rate:.2f} =       {tax_amount.tax:,.2f}")
        print("----------------------------------")
        print(f"              Total =     {self.total:,.2f}")


    @property
    def taxes(self) -> float:
        """Calculates the taxes owed

        As it's calculating the taxes, it is also populating the tax_amounts list
        which stores the Taxed named tuples.

        Returns:
            float -- The amount of taxes owed
        """
        num = self.income
        self.tax_amounts = []
        total_tax = 0
        for bracket in self.tax_bracket:
            if bracket.end < num:
                num -= bracket.end
                self.tax_amounts.append(Taxed(amount=bracket.end, rate=bracket.rate, tax=bracket.end * bracket.rate))
                total_tax += self.tax_amounts[-1].tax
            else:
                self.tax_amounts.append(Taxed(amount=num, rate=bracket.rate, tax=num * bracket.rate))
                total_tax += self.tax_amounts[-1].tax
                break
        return total_tax

    @property
    def total(self) -> float:
        """Calculates total taxes owed

        Returns:
            float -- Total taxes owed
        """
        return self.taxes

    @property
    def tax_rate(self) -> float:
        """Calculates the actual tax rate

        Returns:
            float -- Tax rate
        """
        return self.total / self.income


if __name__ == "__main__":
    salary = 40_000
    t = Taxes(salary)
    t.report()