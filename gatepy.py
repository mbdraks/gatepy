#!/usr/bin/python

# Sample requests to FGT API

import requests, json, sys

# Functions
def api_request(method, params=None):
    'requests methods to api_url and prints the result in json decoded format'
    r = s.get(api_url + method)
    print 'status:', r.status_code
    #print r.json()
    print r.text

def api_post(method, params=None, data=None):
    'post to api_url in json encoded format'
    r = s.post(api_url + method, params=params, data=repr(data))
    print 'status:', r.status_code
    print r.text



#MAIN

cli_usage = '\nUsage: Please specify FortiGate IP Address and VDOM (default to root if not specified\n'

if __name__ == '__main__':
    # Parse for CLI arguments
    if len(sys.argv) > 3:
        # Requires FGT IP and VDOM
        print cli_usage 
        exit()
    else:
        if len(sys.argv) == 3:
            ipaddr = 'http://' + sys.argv[1]
            vdom = sys.argv[2]
        else:
            if len(sys.argv) == 2:
                ipaddr = 'http://' + sys.argv[1]
                vdom = 'root'
            else:
                print cli_usage 
                exit()


# URL definition
login_url = ipaddr + '/logincheck'
logout_url = ipaddr + '/logout'
api_url = ipaddr + '/api/v2/'

# Start session to keep cookies
s = requests.Session()

# Login
# REMEMBER TO CHANGE THIS TO YOUR USER
payload = {'username':'api_user', 'secretkey':'api_pass'}
r = s.post(login_url, data=payload)

print 'login status:', r.status_code
print r.text
print s.cookies['ccsrftoken']


for cookie in s.cookies:
    if cookie.name == 'ccsrftoken':
        csrftoken = cookie.value[1:-1]
        s.headers.update({'X-CSRFTOKEN': csrftoken})
        
#csrftoken = s.cookies['ccsrftoken']
#s.headers.update({'X-CSRFTOKEN': csrftoken})

# Requests
api_request('monitor/system/interface?interface_name=port1')
#api_request('monitor/system/interface/')
#api_request('monitor/system/firmware')
#api_request('cmdb/firewall/address/R1')

# Object creation
payload = {'json':
            {
            'name':'address1',
            'subnet':'2.2.2.2/32'
            }
        }

api_post('cmdb/firewall/address', params={'vdom':vdom}, data=payload)

print r.status_code
print r.text

# Logout
r = s.get(logout_url)
print r.text
