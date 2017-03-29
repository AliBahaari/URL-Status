# URL Status

URL Status Is A Python Script In Order To Retrieve All Links In A Website & Check The Status Of Them. After Checking All Links Status, It Saves The Links That Have 200 Or 404 Status Code With Their Status Code & Message In A File Which User Choose Its Name.<br>
It Is Used In Some SEO-Checker Sites To Check There Is No 404 Error In Website Links.

# Tutorial

Steps To Check A Site :

1. Import URLStatus Class From URLStatus File 
2. Create An Object From URLStatus
3. First Parameter Is Website URL (With Protocol) & Second One Is The File Name That Logs Save In It
4. Then Use ```get_url``` Method To Run Operation On The Website Links & Save Logs To The File (The File Automaticlly Will Be Created)
```python
from URLStatus import URLStatus

url_status = URLStatus('http://www.winatis.ir', 'Links Status')
url_status.get_url()
```
5. Save In A File With ```.py``` Suffix Like ```URL.py``` & Run It With This Command :
```python3 URL.py```

6. You See The Results In Terminal & A File That Logs Has Been Saved In That 

Note : Test File Attached !

# Methods

URLStatus Has 2 Methods :

1. ```get_url``` (Mentioned Its Works)
2. ```clear_file``` (All Logs Append In A File, So If You Want To Clear The File Contents, Use This Method As Below) :
```python
from URLStatus import URLStatus

url_status = URLStatus('http://www.example.com', 'Links Status')
url_status.clear_file()
```

# Exceptions

For Some URLs That Are Not Valid, Used Exceptions To Inform You What Is The Problem & Will Not Be Saved In The File.

# Modules

I Have Used "Requests" & "BeautifulSoup" For This Work.

# Contribute
Please Contribute To Save More Status Codes Links Like 503 & ... (At The Moment It Just Saves 200 & 404 Links)

Thanks !
