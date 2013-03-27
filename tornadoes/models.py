# -*- coding: utf-8 -*-

import json
import threading


class BulkList(object):

    def __init__(self):
        self.lock = threading.RLock()
        with self.lock:
            self.bulk_list = []

    def add(self, index, source):
        with self.lock:
            command = {"_index": index} if index else {}
            source = "%s\n%s" % (json.dumps(command), json.dumps(source))
            self.bulk_list.append(source)

    def prepare_search(self):
        with self.lock:
            source = "\n".join(self.bulk_list) + "\n"
            self.bulk_list = []
            return source
