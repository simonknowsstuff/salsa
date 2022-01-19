import zipfile
from io import BytesIO
from markdown import markdown

TAG_TYPES = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p']

PAGE_BEGIN = '<!DOCTYPE html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>'
PAGE_TITLE_END = '</title></head><body>'
PAGE_END = '</body></html>'


## Local tools
def write_file(path: str, content:str):
  file = open(path, "w+")
  file.write(content)
  file.close()

def readify_as_html(page_title: str, content: str):
  final_html: str
  final_html = PAGE_BEGIN + page_title + PAGE_TITLE_END + markdown(content) + PAGE_END
  return final_html

# Zipping code here
# Credit to https://newseasandbeyond.wordpress.com/2014/01/27/creating-in-memory-zip-file-with-python/
def save_to_user(final_html: str):
  buff = BytesIO()

  with zipfile.ZipFile(buff, mode="w",compression=zipfile.ZIP_DEFLATED) as zf:
    zf.writestr('index.html', final_html)

  return buff.getvalue()

