# URL Status

**URL Status** is a ***Python*** script in order to retrieve all links from a website to check their status. After checking, It saves the links having 200 or 404 status code and in a file which user choose its name.

It is used in some ***Seo Checker*** sites to check there is no 404 error in website links.

## Version 1 to 2

In version 1, You had low performance and speed because logs saved individually, But in version 2, The script saves all logs one time.
Also logs have better view than the version 1.

## Tutorial

Steps :

1. Import `urlstatus` class from ***URLStatus*** file 
2. Create an object from `urlstatus`
3. First parameter is website URL (With protocol) and second one is the file name that logs save in it
4. Then use `get_url` method for running script
```python
from urlstatus import urlstatus

url_status = urlstatus('http://www.example.com', 'links status')
url_status.get_url()
```
5. Save in a file with `.py` extension like `URL.py` and run it with this command :
`python3 URL.py`

6. You see the results in your terminal and a file that logs has been saved in that 

Note : Test file attached.

## Methods

URLStatus has 2 methods :

1. `get_url` (Mentioned its works)
2. `clear_file` (All logs append in a file, So if you want to clear the file contents, Use this method as below) :
```python
from urlstatus import urlstatus

url_status = urlstatus('http://www.example.com', 'links status')
url_status.clear_file()
```

## Exceptions

For some URLs that are not valid, Used exceptions to inform you what is the problem and they will not be saved in the file.

## Modules

The script uses ***requests*** (`get` method), ***BeautifulSoup*** (`bs4` class) and ***json*** (`dumps` method).

## Contribute
Please contribute to save more links that have other status codes like 503 and etc.
