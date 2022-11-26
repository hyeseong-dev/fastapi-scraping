import copy
import uuid
from cassandra.cqlengine.management import sync_table
from .models import Product, ProductScrapeEvent

def create_entry(data:dict):
    try:
        asin = data["asin"]
        title = data["title"]
        price_str = data.get('price_str', "-100")
    except KeyError as e:
        print(e)    
    return Product.create(asin=asin, title=title, price_str=price_str)

def create_scrape_entry(data:dict):
    data['uuid'] = uuid.uuid1() # include a timestamp
    return ProductScrapeEvent.create(**data)

def add_scrape_event(data:dict, fresh=False):
    if fresh:
        data = copy.deepcopy(data)
    product = create_entry(data)
    scrape_obj = create_scrape_entry(data)
    return product, scrape_obj