import os
import urllib.parse as urlparse
from scrapy.dupefilter import RFPDupeFilter
from scrapy.utils.request import request_fingerprint

class DupeCarFilter(RFPDupeFilter):
    def __getid(self, url):
        query = urlparse.parse_qs(urlparse.urlparse(url).query)
        if 'id' in query:
            return query['id'][0]
        else:
            return False

    def request_seen(self, request):
        fp = self.__getid(request.url)
        if fp != False:
            if fp in self.fingerprints:
                return True
            self.fingerprints.add(fp)
            if self.file:
                self.file.write(fp + os.linesep)