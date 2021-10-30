TAG_TYPES = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p']

PAGE_BEGIN = '<!DOCTYPE html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>'
PAGE_TITLE_END = '</title></head><body>'
PAGE_END = '</body></html>'

## Local tools
def write_file(path: str, content:str):
  file = open(path, "w+")
  file.write(content)
  file.close()

## Formatting tools
def tag_formatter(tagtype: str, intag_data: str):
  if tagtype not in TAG_TYPES or intag_data == '':
    raise ValueError("Invalid tag type")
  else:
    output = str('<' + tagtype + '>' + intag_data + '</' + tagtype + '>')
    return output

def export_as_html(page_title: str, content: list, export_path: str):
  final_html: str
  final_html = PAGE_BEGIN + page_title + PAGE_TITLE_END
  for line in content:
    final_html += line
  final_html += PAGE_END
  write_file(export_path, final_html)
  return final_html
  
