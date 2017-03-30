from requests import get
from bs4 import BeautifulSoup
from json import dumps


class URLStatus:
    """ Get Website URLs Status ... """

    status_codes = {
        '200 (OK)': [],
        '404 (Not Found)': []
    }

    def __init__(self, url, file_name):
        self.url = url
        self.file_name = file_name

    def get_url(self):
        try:
            request_site = get(self.url)
        except Exception as SiteError:
            print(str(SiteError) + '\n')
        else:
            if request_site.status_code == 200:
                bs = BeautifulSoup(request_site.text, 'lxml')
                for aItem in bs.find_all('a'):
                    href_address = aItem.get('href')
                    try:
                        new_request = get(href_address)
                    except Exception as Error:
                        print(str(Error) + '\n')
                    else:
                        if new_request.status_code == 200:
                            URLStatus.status_codes['200 (OK)'].append(href_address)
                        if new_request.status_code == 404:
                            URLStatus.status_codes['404 (Not Found)'].append(href_address)
                file_open = open(self.file_name + '.txt', 'a')
                file_open.write(str(dumps(URLStatus.status_codes, indent=4)))
                file_open.close()
                print('Saved To File :' + str(URLStatus.status_codes))

    def clear_file(self):
        with open(self.file_name + '.txt', "w"):
            pass
