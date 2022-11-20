import uuid
from cassandra.cqlengine.management import sync_table
from .db import get_session
from .models import Product, ProductScrpeEvent

session = get_session()
sync_table(Product)
sync_table(ProductScrpeEvent)

def create_entry(data:dict):
    return Product.create(**data)

def create_scrape_entry(data:dict):
    data['uuid'] = uuid.uuid1() # include a timestamp
    return ProductScrpeEvent.create(**data)

def add_scrape_entry(data:dict):
    product = create_entry(data)
    scrape_obj = create_scrape_entry(data)
    return product, scrape_obj

data = {
     "asin": "AMSMSMDMFDF",
     "title": "MARK 1"
 }