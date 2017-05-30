import feedparser

class NistLatest(object):
    """
    Class for reading the first item in the NVD RSS feed
    Add the following command to your action.py file 
    make_actor function.

    actor.add_keyword(_('nvd latest'), NistLatest(say))

    """

    def __init__(self, say):

        self.nvd_rss_url = "https://nvd.nist.gov/download/nvd-rss.xml"
        self.say = say

    def run(self, command):

        feed = feedparser.parse(self.nvd_rss_url)
        self.say(feed['entries'][0]['title'])
        self.say(feed['entries'][0]['summary'])


