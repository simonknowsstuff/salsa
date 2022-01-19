## This code tests the main por_utilities API made for salsa.

from flask import Flask, render_template, request, Response
app = Flask(__name__)
import por_utilities as por_utils

page_attributes = {
  'name':'',
  'short_description':'',
  'long_description':''
}

@app.route('/', methods=["GET", "POST"])
def main():
  if request.method == "POST":
    page_attributes['name'] = request.form.get("websitename")
    page_attributes['markdown'] = request.form.get("markdown")
    
    # Messy code (will remove)
    html_content = page_attributes['markdown']
    
    # Returns html code
    final_html = por_utils.readify_as_html(page_attributes['name'], html_content)
    return Response(por_utils.save_to_user(final_html), mimetype="application/zip")
  return render_template('index.html')

# page_attributes = {'page_title': str, 'css_path': str}
# html_content: list = []
# por_utilities.export_as_html('Title', html_content, 'test.html')

app.run(host='0.0.0.0', port=5000, debug=True) # Run the Application (in debug mode)