import re
import sys
import urllib2
import urlparse
 
from bs4 import BeautifulSoup
 
 
 
class Crawler(object):
 
    def __init__(self, urls):
        self.urls = [urls]
     
     
     
    def crawl(self):
    child =[]
    chilmail = set()
    mailbox = set()
    haslink=True
    emailcount=0
 
     
        for url in self.urls:
        data = self.request(url)
        soup = BeautifulSoup(data,"html.parser")
        mailto = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+",data,re.I))
        mailbox = mailto | mailbox
         
         
        for link in soup.find_all("a"):
        try:
                    links = link.attrs["href"]
        except:
            links =""                           
        if links.startswith('..'):
            links =url+links[2:]
        elif links.startswith('.'):
            links =url+links[1:]
        elif links.startswith('/'):
            links = url+links
        elif 'http' not in links:
            links="http://"+url+"/"+links
        else:
            links=links
             
        if links not in self.urls and len(self.urls)<=100:
                self.urls.append(links)
    print len(mailbox)
    for data in mailbox:
        print data
    ''' 
    for url in child:
        data = self.request(url)
        chilmails = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+",data,re.I))
            chilmail = chilmail | chilmails
        chilmail = chilmail | mailbox
    print "The numbers of emails has",len(chilmail)
    for data in chilmail:
        print data
    '''
    @staticmethod
    def request(url):
    if 'http' not in url:
        url="http://"+url   
        try:
            response = urllib2.urlopen(url)
    except:
        return ""
    return response.read()
   
def main():
    urls=sys.argv[1]
    crawler = Crawler(urls)
    crawler.crawl()
 
     
if __name__ == '__main__':
  sys.exit(main())
