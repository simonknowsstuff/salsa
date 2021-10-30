## This code tests the main por_utilities API made for salsa.

import por_utilities

page_attributes = {
  'page_title':str,
  'css_path':str
}

html_content: list = ['<p>Test</p>', '<h1>Heading</h1>', '<p>Paragraph</p>']

por_utilities.export_as_html('Title', html_content, 'test.html')
