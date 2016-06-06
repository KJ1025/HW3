import re
import sys
import urllib2
import urlparse

class Crawler(object):

    def __init__(self, urls):
        self.urls = urls.split(',')
	i=0
	for url in self.urls:
   	    if 'http' not in self.urls[i]:
		self.urls[i]="http://"+self.urls[i]
		i=i+1
	    else:
		i=i+1
	

    
    def crawl(self):
	emailcount=0
       
        for url in self.urls:
            data = self.request(url)
	    print "***********************"+"\n"+url+" email:"
            for email in self.process(data):
		emailcount=emailcount+1
	        print email,emailcount

    @staticmethod
    def request(url):
        try:
            response = urllib2.urlopen(url)
	    return response.read()
	except:
	    print "\nWrong urls with\n"+url
	    sys.exit()
    @staticmethod
    def process(data):
        
        for email in re.findall(r'(\w+@\w+\.com)', data):
            yield email


def main():
    urls=sys.argv[1]
    crawler = Crawler(urls)
    crawler.crawl()
#ex:http://www.ee.ccu.edu.tw/members/teacher.php
    
if __name__ == '__main__':
  sys.exit(main())
