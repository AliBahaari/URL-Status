# Test

from URLStatus import URLStatus
from requests import get
test_url_status = URLStatus('http://www.dartil.com', 'Links Status')
test_url_status.get_url()
