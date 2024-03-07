import pandas as pd
import re
from time import sleep

DATA_FILE_NAME = "data/MHMP_dopravni_prestupky_2023.csv"
def clean_address(address: str):
    match_address = address.replace("u domu","")
    match_address = re.search(r"(\w+\s)+(\d+\/\d+|\d+)", match_address)
    if match_address:
        print(f'"{match_address.group()}"|"{address}"')

        return match_address.group()
    else:
        return ""



