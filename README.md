# requests_refresh_header.py

## Description

This package implements support for Refresh header in the ```requests``` package, where the header is not treated as special. The `Refresh` header is commonly used to support the client-side polling of resources. The Refresh header is not defined by any specification, so this package aims to handle it similarly to most browsers. 

## Usage

This package relies on the `requests` package's hook feature. This feature is used by `requests_refresh_header` to check for and handle any responses with a valid `Refresh` header. 

For further reading, check out the [official requests documentation on event hooks](https://requests.readthedocs.io/en/latest/user/advanced/#event-hooks).

### Example

The hook can be passed into a single request, like so.

```python
import requests
from requests_refresh_header import hook as refresh_hook

# If a valid Refresh header is detected it will be handled by the hook.
response = requests.get('https://www.google.com/', hooks={'response': [refresh_hook]})
```

It can also be added to a session.

```python
import requests
from requests_refresh_header import hook as refresh_hook

session = requests.session(hooks={'response': [refresh_hook]})

session.get('https://www.google.com/') # Refresh header will be handled for any requests from this session.
```

## Design

The header is not defined in the HTTP spec. However, it is mentioned in WHATWG as being [equivalent to the Refresh meta tag](https://html.spec.whatwg.org/dev/document-lifecycle.html#the-refresh-header). This package simulates the behavior described for the meta refresh tag with more liberal parsing (such as accepting ',' or ';' as a seperator between the time and the URL) since not all sites strictly adhere the exact format described by WHATWG.
