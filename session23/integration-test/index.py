import os
import testcontainers.compose

COMPOSE_PATH = os.getcwd() 

def get_db_conn():
  """function returning the DB psycopg2 connection."""
  conn = psycopg2.connect(
    host="localhost",
    database="cs162",
    user="cs162_user",
    password="cs162_password")
  
  return conn

def setup_module():
  compose = testcontainers.compose.DockerCompose(COMPOSE_PATH)
  compose.start()
  time.sleep(10)
  return compose, get_db_conn()

def teardown_module(compose):
  compose.stop()

def test_db():
  compose = setup_module()
  
  # Test 1: Check DB accepts connections
  cur = conn.cursor()
  cur.execute(“SELECT ‘foo’”)
  assert cur.fetchone()[0] == “foo”, “Database is not running”
  cur.close()
  teardown_module(compose)