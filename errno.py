# -*- coding: utf-8 -*-

import os
import sys
import errno
import json

data = {
    "items": []
}

def getNumber(query):
    for no in errno.errorcode:
        if errno.errorcode[no] == query:
            return no

    return int(query)

def formatItem(no):
    name = errno.errorcode[no]
    title = "{}({})".format(name, no)
    subtitle = os.strerror(no)
    item = {
        "title": title,
        "subtitle": subtitle,
        "arg": name
    }
    return item

query = sys.argv[1]
if len(query) > 0:
    try:
        no = getNumber(query)
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
