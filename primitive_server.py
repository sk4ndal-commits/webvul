import requests
from multiprocessing import Queue, Process
from myserver import SimpleHTTPRequestHandler
import sqlite3
from http.server import HTTPServer

HTTPD_MESSAGE_QUEUE = Queue()

def print_httpd_messages():
  while not HTTPD_MESSAGE_QUEUE.empty():
    message = HTTPD_MESSAGE_QUEUE.get()
    print(message)

def clear_httpd_messages():
  while not HTTPD_MESSAGE_QUEUE.empty():
    HTTPD_MESSAGE_QUEUE.get()

def webbrowser(url, mute):
  try:
    r = requests.get(url)
    contents = r.text
  finally:
    if not mute:
      print_httpd_messages()
    else:
      clear_httpd_messages()
  
  return contents

def run_httpd_forever(handler_class):
  host = '127.0.0.1'

  for port in range(8800, 9000):
    print('trying port {}'.format(port))

    httpd_address = (host, port)

    try:
      httpd = HTTPServer(httpd_address, handler_class)
      break
    except OSError:
      continue
  
  httpd_url = 'http://'+host+':'+repr(port)
  HTTPD_MESSAGE_QUEUE.put(httpd_url)
  httpd.serve_forever()

def start_httpd(handler_class = SimpleHTTPRequestHandler):
  clear_httpd_messages()

  httpd_process = Process(target=run_httpd_forever, args=(handler_class,))
  httpd_process.start()

  httpd_url = HTTPD_MESSAGE_QUEUE.get()
  return httpd_process, httpd_url
 
def init_db():
  db_connection = sqlite3.connect('orders.db')
  db_connection.execute('DROP TABLE IF EXISTS orders')
  db_connection.execute('CREATE TABLE orders (item, name, email, city, zip)')
  db_connection.commit()

  return db_connection

if __name__ == '__main__':
  db = init_db()
  httpd_process, httpd_url = start_httpd()

  print(httpd_url)
  print('hello')


