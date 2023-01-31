"""
Python Program – Search Keys in a Dictionary

Let’s assume that our program has a dictionary of fortune 500 companies and their world ranking.
Task is to search keys in the dictionary which are at world ranking 5.
"""
from typing import List

'''
Get a list of Companies from dictionary having a specfied rank
'''

# Dictionary of fortune 500 companies
dictOfFortune500 = {
    "Walmart": 1,
    "Exxon Mobil": 2,
    "Berkshire Hathaway": 3,
    "Apple": 4,
    "UnitedHealth Group": 5,
    "McKesson": 5,
    "CVS Health": 5,
    "Amazon.com": 6,
    "AT&T": 6,
    "General Motors": 7
}

def get_company_by_ranking(companies:dict, rank:List[int]) -> List[str]:
    return list(map(lambda item: item[0],
                    filter(lambda item: item[1] in rank, companies.items())))

if __name__ == '__main__':
   rank5_comps =  get_company_by_ranking(dictOfFortune500, [5, 6])
   print(rank5_comps)

