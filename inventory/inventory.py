#!/usr/bin/env python

import json
import os
import sys


INVENTORY_DATA = '''{
    "_meta": {
        "hostvars": {
            "server00": {
                "ansible_connection": "local"
            },
            "server01": {
                "ansible_connection": "local"
            }
        }
    },
    "testservers": {
        "hosts": [
            "server00",
            "server01"
        ],
        "vars": {}
    }
}'''

if __name__ == '__main__':
    try:
        inventory_data = json.loads(INVENTORY_DATA)
        host_filter = os.environ['HOST_FILTER']
        inventory_data['_meta']['hostvars'].pop(host_filter)
        inventory_data['testservers']['hosts'].remove(host_filter)
    except KeyError:
        pass

    if sys.argv[1] == '--list':
        print(json.dumps(inventory_data))

#
# EOF
#
