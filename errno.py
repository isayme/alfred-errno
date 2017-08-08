import os
import sys
import errno
import json

data = {
    "items": []
}

def formatItem(no):
    title = errno.errorcode[no]
    subtitle = os.strerror(no)
    item = {
        "title": title,
        "subtitle": subtitle,
        "arg": title
    }
    return item

query = sys.argv[1]
if len(query) > 0:
    try:
        no = int(query)
        item = formatItem(no)
    except Exception as e:
        item = {
            "title": 'Not Found',
            "subtitle": "typo errno / no such a errno",
            "icon": {
                "path": "./warn.png"
            }
        }
    finally:
        data['items'].append(item)
else:
    for no in errno.errorcode:
        data['items'].append(formatItem(no))

print(json.dumps(data))