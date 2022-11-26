from cassandra.cqlengine import columns 
from cassandra.cqlengine.models import Model

# List View -> Detail View
class Product(Model):
    __keyspace__ = "scrapper_app"
    asin = columns.Text(primary_key=True, required=True)
    title = columns.Text()
    price_str = columns.Text(default='-100')

# Detail View for asin
class ProductScrapeEvent(Model):
    __keyspace__ = "scrapper_app"
    uuid = columns.UUID(primary_key=True)
    asin = columns.Text(index=True)
    title = columns.Text()
    price_str = columns.Text(default='-100')
    
# def this -> Product.objects().filter(asin="ASDFASDFASDF")
# not this -> Product.objects().filter(title="Mark 1")