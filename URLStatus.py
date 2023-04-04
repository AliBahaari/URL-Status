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

            if request_site.status_code == 200:
                bs = BeautifulSoup(request_site.text, 'lxml')

                for a_tag in bs.find_all('a'):
                    a_tag_href = a_tag.get('href')
                    try:
                        a_tag_request = get(a_tag_href)

                        if a_tag_request.status_code == 200:
                            self.status_codes['200 (OK)'].append(
                                a_tag_href)
                        if a_tag_request.status_code == 404:
                            self.status_codes['404 (Not Found)'].append(
                                a_tag_href)

                    except:
                        pass
                        print(str(a_tag_href) + " - Can't Be Connected")

                file_open = open(self.file_name + '.txt', 'w')
                file_open.write(str(dumps(self.status_codes, indent=4)))
                file_open.close()
                print('Saved To File :\n' + str(dumps(self.status_codes)))

        except:
            pass
            print("Can't Be Connected")

    def clear_file(self):
        with open(self.file_name + '.txt', "w"):
            pass
