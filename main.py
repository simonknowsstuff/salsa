## This code tests the main por_utilities API made for salsa.
import por_utilities
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def main():
  return render_template('index.html')

page_attributes = {'page_title': str, 'css_path': str}
html_content: list = []
por_utilities.export_as_html('Title', html_content, 'test.html')

app.run(host='0.0.0.0', port=5000, debug=True) # Run the Application (in debug mode)