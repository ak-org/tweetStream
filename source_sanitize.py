import os
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):

   #Initializing lists
   lsStartTags = list()
   lsEndTags = list()
   lsStartEndTags = list()
   lsComments = list()
   lsContents = list()

   #HTML Parser Methods
   def handle_starttag(self, startTag, attrs):
       self.lsStartTags.append(startTag)

   def handle_endtag(self, endTag):
       self.lsEndTags.append(endTag)

   def handle_startendtag(self,startendTag, attrs):
       self.lsStartEndTags.append(startendTag)

   def handle_comment(self,data):
       self.lsComments.append(data)


   def handle_data(self,data):
       self.lsContents.append(data)       

def parsed_values(source):
    #creating an object of the overridden class
    parser = MyHTMLParser()
    parser.lsStartTags = []
    parser.lsEndTags = []
    parser.lsStartEndTags = []
    parser.lsComments = []
    parser.lsContents = []

    #Feeding the content
    parser.feed(source)

    return parser.lsContents[0]


if __name__ == "__main__":

    source1 = "\u003ca href=\"http:\/\/twitter.com\/download\/iphone\" rel=\"nofollow\"\u003eTwitter for iPhone\u003c\/a\u003e"
    source2 = "\u003ca href=\"http:\/\/twitter.com\" rel=\"nofollow\"\u003eTwitter Web Client\u003c\/a\u003e"
    source3 = "\u003ca href=\"http:\/\/twitter.com\/download\/android\" rel=\"nofollow\"\u003eTwitter for Android\u003c\/a\u003e"
    source4 = "\u003ca href=\"http:\/\/twitter.com\/#!\/download\/ipad\" rel=\"nofollow\"\u003eTwitter for iPad\u003c\/a\u003e"
    source5 = "\u003ca href=\"https:\/\/mobile.twitter.com\" rel=\"nofollow\"\u003eTwitter Lite\u003c\/a\u003e"
    source6 = "\u003ca href=\"http:\/\/twitter.com\" rel=\"nofollow\"\u003eTwitter Web Client\u003c\/a\u003e"


    print(parsed_values(source1))
    print(parsed_values(source2))
    print(parsed_values(source3))
    print(parsed_values(source4))
    print(parsed_values(source5))
    print(parsed_values(source6))    