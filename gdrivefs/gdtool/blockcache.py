import os


class BlockCache(object):
    entry_id = None
    offset = 0
    size = 0

    def __init__(self, entry_id, offset, size):
        self.entry_id = entry_id
        self.offset = offset
        self.size = size

    def get_cache_file(self):
        filename = '%s-%s-%s' % (self.entry_id, self.offset, self.size)
        path = os.path.join('/tmp', filename)
        return path

    def get(self):
        path = self.get_cache_file()
        r = None
        if os.path.exists(path):
            with open(path, 'rb') as f:
                r = f.read()
        return r

    def set(self, content):
        path = self.get_cache_file()
        with open(path, 'wb') as f:
            f.write(content)
