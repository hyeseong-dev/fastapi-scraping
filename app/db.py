import logging

log = logging.getLogger()
log.setLevel('DEBUG')
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s"))
log.addHandler(handler)

from cassandra import ConsistencyLevel
from cassandra.cluster import Cluster
from cassandra.query import SimpleStatement

KEYSPACE = "scraper_app"


def get_cluster():
    log.info("connecting cassandra...")
    return Cluster(['127.0.0.1'])

def set_settion(session):
    log.info('set settion...')
    session.execute("""
        CREATE KEYSPACE IF NOT EXISTS %s
        WITH replication = { 'class': 'SimpleStrategy', 'replication_factor': '2' }
        """ % KEYSPACE)
    session.set_keyspace(KEYSPACE)

def get_session():
    log.info("get setssion....")
    session = None
    cluster = get_cluster()
    session = cluster.connect()
    set_settion(session)
    return session

if __name__ == "__main__":    
    session = get_session()
    row = session.execute('select release_version from system.local').one()
    if row:
        print(row[0])
    else :
        print("An error occurred")
 