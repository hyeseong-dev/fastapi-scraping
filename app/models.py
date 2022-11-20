from cassandra.cqlengine import columns 
from cassandra.cqlengine.models import Model

class Product(Model):
    __keyspace__ = "scrapper_app"
    asin: columns.Text(primary_key=True, required=True)
    title: columns.Text()
    
# def this -> Product.objects().filter(asin="ASDFASDFASDF")
# not this -> Product.objects().filter(title="Mark 1")