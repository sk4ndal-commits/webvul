HTML_TERMS_AND_CONDITIONS = """
<html><body>
<div style="border:3px; border-style:solid; border-color:#FF0000; padding: 1em;">
  <strong id="title" style="font-size: x-large">Fuzzingbook Terms and Conditions</strong>
  <p>
  The content of this project is licensed under the
  <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons
  Attribution-NonCommercial-ShareAlike 4.0 International License.</a>
  </p>
  <p>
  To place an order, use our <a href="/">order form</a>.
  </p>
</div>
</body></html>
"""

HTML_ORDER_RECEIVED = """
<html><body>
<div style="border:3px; border-style:solid; border-color:#FF0000; padding: 1em;">
  <strong id="title" style="font-size: x-large">Thank you for your Fuzzingbook Order!</strong>
  <p id="confirmation">
  We will send <strong>{item_name}</strong> to {name} in {city}, {zip}<br>
  A confirmation mail will be sent to {email}.
  </p>
  <p>
  Want more swag?  Use our <a href="/">order form</a>!
  </p>
</div>
</body></html>
"""

HTML_ORDER_FORM = """
<html><body>
<form action="/order" style="border:3px; border-style:solid; border-color:#FF0000; padding: 1em;">
  <strong id="title" style="font-size: x-large">Fuzzingbook Swag Order Form</strong>
  <p>
  Yes! Please send me at your earliest convenience
  <select name="item">
  """
# (We don't use h2, h3, etc. here
# as they interfere with the notebook table of contents)

FUZZINGBOOK_SWAG = {
    "tshirt": "One FuzzingBook T-Shirt",
    "drill": "One FuzzingBook Rotary Hammer",
    "lockset": "One FuzzingBook Lock Set"
}

for item in FUZZINGBOOK_SWAG:
    HTML_ORDER_FORM += \
        '<option value="{item}">{name}</option>\n'.format(item=item,
            name=FUZZINGBOOK_SWAG[item])

HTML_ORDER_FORM += """
  </select>
  <br>
  <table>
  <tr><td>
  <label for="name">Name: </label><input type="text" name="name">
  </td><td>
  <label for="email">Email: </label><input type="email" name="email"><br>
  </td></tr>
  <tr><td>
  <label for="city">City: </label><input type="text" name="city">
  </td><td>
  <label for="zip">ZIP Code: </label><input type="number" name="zip">
  </tr></tr>
  </table>
  <input type="checkbox" name="terms"><label for="terms">I have read
  the <a href="/terms">terms and conditions</a></label>.<br>
  <input type="submit" name="submit" value="Place order">
</p>
</form>
</body></html>
"""

HTML_NOT_FOUND = """
<html><body>
<div style="border:3px; border-style:solid; border-color:#FF0000; padding: 1em;">
  <strong id="title" style="font-size: x-large">Sorry.</strong>
  <p>
  This page does not exist.  Try our <a href="/">order form</a> instead.
  </p>
</div>
</body></html>
  """

HTML_INTERNAL_SERVER_ERROR = """
<html><body>
<div style="border:3px; border-style:solid; border-color:#FF0000; padding: 1em;">
  <strong id="title" style="font-size: x-large">Internal Server Error</strong>
  <p>
  The server has encountered an internal error.  Go to our <a href="/">order form</a>.
  <pre>{error_message}</pre>
  </p>
</div>
</body></html>
  """