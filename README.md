# URL Status

***URL Status*** retrieves all links from a website to check their status. After checking, it saves the links having 200 or 404 HTTP status code in a file choosing its name.

## Tutorial

1. Import `urlstatus` class from ***URLStatus*** file 
2. Create an object from `urlstatus`
3. First parameter is the website URL (with protocol) and second one is the file name
4. Then call `get_url` method
```python
from urlstatus import urlstatus

url_status = urlstatus('http://www.example.com', 'links status')
url_status.get_url()
```
5. Save in a file with `.py` extension like `URL.py` and run it with this command :
`python3 URL.py`
6. You see the results in your terminal and a file that logs have been saved in it 

All logs append in the file, so if you want to clear the file contents, use the method below) :
```python
url_status.clear_file()
```

## Modules

Uses *requests* (`get` method), *bs4* (`BeautifulSoup` class) and *json* (`dumps` method).

## Contribute
It should save other HTTP status codes - 502, 503, 599, etc.
