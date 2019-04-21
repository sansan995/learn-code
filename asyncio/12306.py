import requests
from requests.packages import urllib3
from requests.exceptions import ReadTimeout, HTTPError, RequestException

urllib3.disable_warnings()
try:
    response = requests.get('https://www.12306.cn', verify=False, timeout = 0.5)
    print(response.status_code)
except ReadTimeout:
    print('timeout')
except HTTPError:
    print('httperror')
except RequestException:
    print(requestsexception)
