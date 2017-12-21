from html.parser import HTMLParser
from urllib import parse


class LinkFinder(HTMLParser): #inherits form HTMLParser
#call super class initialization methods. Base = homepage, page_url = page you are crawling
    def __init__(self, base_url, page_url): #needs two urls for base and page
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()

    # When we call HTMLParser feed() this function is called when it encounters an opening tag <a>
    def handle_starttag(self, tag, attrs): #called whenever it comes across a start tag. ex: <a href
        if tag == 'a': #means its a link. a for anchor
            for (attribute, value) in attrs: #
                if attribute == 'href':
                    url = parse.urljoin(self.base_url, value) #cant use relative path, we need full URL.
                    self.links.add(url) #going to add a properly formatted url to our set of links.

    def page_links(self): #returns set of links
        return self.links

    def error(self, message): #required initialization method from htmlParser
        pass

