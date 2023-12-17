import logging
import requests
from src.requests_refresh_header import create_hook

# Set logging level.
logging.basicConfig(level=logging.DEBUG)

# Create a session.
session = requests.Session()

# Register the hook.
session.hooks['response'].append(create_hook(5))

# Set proxy.
session.proxies = {
    'https': 'socks5h://localhost:9050',
    'http': 'socks5h://localhost:9050'
}

# Make a request.
r = session.get('http://g66ol3eb5ujdckzqqfmjsbpdjufmjd5nsgdipvxmsh7rckzlhywlzlqd.onion')
print(r.from_refresh)

