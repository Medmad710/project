from OZON_parcer import PriceFindOZON
from WB_parser import PriceFindWB

def PriceFind(url):
    if "wildberries" in url:
        return PriceFindWB
    if "ozon" in  url:
        return PriceFindOZON