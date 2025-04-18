# utils.py
import urllib.parse

def encode_url(url):
    return urllib.parse.quote(url,safe='')

def decode_url(encoded_url):
    return urllib.parse.unquote(encoded_url)
