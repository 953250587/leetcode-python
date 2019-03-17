"""
    Note: This is a companion problem to the System Design problem: Design TinyURL.

TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.

Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.


"""


class Codec:
    urls = []

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        self.urls.append(longUrl)
        return str(len(self.urls) - 1)

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        index = int(shortUrl)
        return self.urls[index] if index < len(self.urls) else ''


        # Your Codec object will be instantiated and called as such:
        # codec = Codec()
        # codec.decode(codec.encode(url))