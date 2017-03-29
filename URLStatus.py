from requests import get
from bs4 import BeautifulSoup


class URLStatus:
    """ Get Website URLs Status ... """

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
                        file_open = open(self.file_name + '.txt', 'a')
                        if new_request.status_code == 200:
                            file_open.write(href_address + ' - 200 (OK)\n\n')
                            print('Saved To File :' + href_address + ' - 200 (OK)\n')
                        if new_request.status_code == 404:
                            file_open.write(href_address + ' - 404 (Not Found)\n\n')
                            print('Save To File :' + href_address + ' - 404 (Not Found)\n')
                        file_open.close()

    def clear_file(self):
        with open(self.file_name + '.txt', "w"):
            pass
