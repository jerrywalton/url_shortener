# url_shortner.py
# python code to shorten an url
# author: Jerry Walton
import hashlib


class URLShortener:
    def __init__(self):
        self.url_map = {}
        self.base_url = "https://short.url/"

    def shorten_url(self, long_url):
        hash_value = hashlib.md5(long_url.encode()).hexdigest()[:8]
        short_url = self.base_url + hash_value
        self.url_map[short_url] = long_url
        return short_url

    def expand_url(self, short_url):
        if short_url in self.url_map:
            return self.url_map[short_url]
        else:
            return "URL not found"


if __name__ == "__main__":
    url_shortener = URLShortener()

    # first example
    long_url = "https://www.symboliclanguages.com"
    short_url = url_shortener.shorten_url(long_url)
    print(f"original url: {long_url}")
    print(f"shortened url: {short_url}")
    expanded_url = url_shortener.expand_url(short_url)
    print(f"Expanded URL: {expanded_url}")

    # second example
    another_url = "https://www.example.com/another/long/url"
    another_short_url = url_shortener.shorten_url(another_url)
    print(f"Original URL: {another_url}")
    print(f"Shortened URL: {another_short_url}")
    expanded_url_2 = url_shortener.expand_url(another_short_url)
    print(f"Expanded URL: {expanded_url_2}")
