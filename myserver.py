from http.server import HTTPServer, BaseHTTPRequestHandler, HTTPStatus
from myforms import *
import urllib.parse
import traceback
import sqlite3


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
  def do_HEAD(self):
    self.send_response(HTTPStatus.OK)
    self.send_header('Content-type', 'text/html')
    self.end_headers()

  def do_GET(self):
    try:
      if self.path == "/":
        print('path started with /')
        self.send_order_form()
      elif self.path.startswith("/order"):
        self.handle_order()
      elif self.path.startswith("/terms"):
        self.send_terms_and_conditions()
      else:
        self.not_found()
    except Exception:
      self.internal_server_error()
  
  def send_order_form(self):
    self.send_response(HTTPStatus.OK, 'Place your order')
    self.send_header('Content-type', 'text/html')
    self.end_headers()
    self.wfile.write(HTML_ORDER_FORM.encode('utf8'))
  
  def send_terms_and_conditions(self):
    self.send_response(HTTPStatus.OK, 'Terms and Conditions')
    self.send_header('Content-type', 'text/html')
    self.end_headers()
    self.wfile.write(HTML_TERMS_AND_CONDITIONS.encode('utf8'))
  
  def get_field_values(self):
    query_string = urllib.parse.urlparse(self.path).query
    fields = urllib.parse.parse_qs(query_string, keep_blank_values=True)

    values = {}

    for key in fields:
      values[key] = fields[key][0]
    
    return values

  def handle_order(self):
    values = self.get_field_values()
    self.store_order(values)
    self.send_order_received(values)
  
  def store_order(self, values):
    db = sqlite3.connect('orders.db')
    sql_query = "INSERT INTO orders VALUES ('{item}','{name}','{email}','{city}','{zip}')".format(**values)
    self.log_message("%s", sql_query)
    db.executescript(sql_query)
    db.commit()
  
  def send_order_received(self, values):
    values['item_name'] = FUZZINGBOOK_SWAG[values['item']]
    confirmation = HTML_ORDER_RECEIVED.format(**values).encode('utf8')

    self.send_response(HTTPStatus.OK, 'Order received')
    self.send_header('Content-type', 'text/html')
    self.end_headers()
    self.wfile.write(confirmation)
  
  def not_found(self):
    self.send_response(HTTPStatus.NOT_FOUND, 'Not found')
    self.send_header('Content-type', 'text/html')
    self.end_headers()
    self.wfile.write(HTML_NOT_FOUND.encode('utf8'))
  
  def internal_server_error(self):
    self.send_response(HTTPStatus.INTERNAL_SERVER_ERROR, 'Internal error')
    self.send_header('Content-type', 'text/html')
    self.end_headers()

    exc = traceback.format_exc()
    self.log_message('%s', exc.strip())

    self.wfile.write(HTML_INTERNAL_SERVER_ERROR.format(error_message=exc).encode('utf8'))