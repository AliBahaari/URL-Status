# URL Status

![Python Badge](https://alibahaari.github.io/Badge/Python.png)

***URL Status*** retrieves all links from a website to check their status, then it saves the links having 200 or 404 HTTP status code in a file choosing its name.

## Tutorial

1. Import `urlstatus` class from ***URLStatus*** module 
2. Create an object from `urlstatus`
3. First parameter is the website URL (with protocol) and the second one is the file name
4. Call `get_url` method
```python
from urlstatus import urlstatus

url_status = urlstatus('http://www.example.com', 'links status')
url_status.get_url()
```
5. Save in a file with `.py` extension like `URL.py` and run it with the command below :
`python3 URL.py`
6. Results will be displayed in terminal and the file

All logs append in the file, so if you want to clear the file contents, use the method below :
```python
url_status.clear_file()
```

## Modules

Used *requests* (`get` method), *bs4* (`BeautifulSoup` class) and *json* (`dumps` method).

## Contribute
It will save other HTTP status codes - 502, 503, 599, etc.
