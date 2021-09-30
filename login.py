import getpass
import sys
import requests
from functools import cached_property

proxy_set = {'btech': 22, 'dual': 62, 'diit': 21, 'faculty': 82, 'integrated': 21, 'mtech': 62, 'phd': 61,
             'retfaculty': 82, 'staff': 21, 'irdstaff': 21, 'mba': 21, 'mdes': 21, 'msc': 21, 'msr': 21, 'pgdip': 21}


class Proxy:

    def __init__(self, username, password, category):
        self.username = username
        self.password = password
        self.category = category

    @cached_property
    def session_id(self):
        return self._get_session_id()

    @property
    def login_form(self):
        return {'sessionid': self.session_id, 'action': 'Validate', 'userid': self.username, 'pass': self.password}

    @property
    def refresh_form(self):
        return {'sessionid': self.session_id, 'action': 'Refresh'}

    @property
    def proxy_page_address(self):
        return f'https://proxy{proxy_set[self.category]}.iitd.ernet.in/cgi-bin/proxy.cgi'

    def login(self):
        response = requests.post(self.proxy_page_address, data=self.login_form, verify=False).text
        if "Either your userid and/or password does'not match." in response:
            return "Incorrect", response
        elif "You are logged in successfully as " + self.username in response:
            return "Success", response
        elif "already logged in" in response:
            return "Already", response
        elif "Session Expired" in response:
            return "Expired", response
        else:
            return "Not Connected", response

    def _get_session_id(self):
        resp = requests.get(self.proxy_page_address, verify=False)
        check_token = 'sessionid" type="hidden" value="'
        token_index = resp.text.index(check_token) + len(check_token)
        session_id = resp.text[token_index:token_index + 16]
        return session_id


if __name__ == "__main__":
    n = len(sys.argv)
    uname = input('Username:')
    passwd = getpass.getpass('Password:')
    proxycat = input('Category(phd or irdstaff):') or 'irdstaff'
    user = Proxy(username=uname, password=passwd, category=proxycat)
    print(user.login())
