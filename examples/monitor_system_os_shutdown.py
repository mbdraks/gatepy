#!/usr/bin/env python3

'''
Immediately shutdown this device.

Method
    https://<DEVICE_IP>/api/v2/monitor/system/os/shutdown


CLI
    NA


Debug
    NA
'''

import os
import json
from fortiosapi import FortiOSAPI


FG = FortiOSAPI()

# Source _host
FG_HOST = os.environ['FG_HOST']
FG_USER = os.environ['FG_USER']
FG_PASS = os.environ['FG_PASS']

DEVICE = {
    'host': FG_HOST,
    'username': FG_USER,
    'password': FG_PASS,
}

FG.login(**DEVICE)

UPLOAD_DATA = {
    'event_log_message': 'going down',
}

UPLOAD_DATA = json.dumps(UPLOAD_DATA)

# Using upload method because it's the easiest way to POST to
# /monitor using fortiosapi at the moment
FG.upload('system', 'os/shutdown', data=UPLOAD_DATA)


'''
Currently this code works but will hang at the end and will raise the following errors:

Traceback (most recent call last):
  File "/usr/local/lib/python3.5/dist-packages/urllib3/connectionpool.py", line 600, in urlopen
    chunked=chunked)
  File "/usr/local/lib/python3.5/dist-packages/urllib3/connectionpool.py", line 384, in _make_request
    six.raise_from(e, None)
  File "<string>", line 2, in raise_from
  File "/usr/local/lib/python3.5/dist-packages/urllib3/connectionpool.py", line 380, in _make_request
    httplib_response = conn.getresponse()
  File "/usr/lib/python3.5/http/client.py", line 1197, in getresponse
    response.begin()
  File "/usr/lib/python3.5/http/client.py", line 297, in begin
    version, status, reason = self._read_status()
  File "/usr/lib/python3.5/http/client.py", line 266, in _read_status
    raise RemoteDisconnected("Remote end closed connection without"
http.client.RemoteDisconnected: Remote end closed connection without response

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/usr/local/lib/python3.5/dist-packages/requests/adapters.py", line 445, in send
    timeout=timeout
  File "/usr/local/lib/python3.5/dist-packages/urllib3/connectionpool.py", line 638, in urlopen
    _stacktrace=sys.exc_info()[2])
  File "/usr/local/lib/python3.5/dist-packages/urllib3/util/retry.py", line 367, in increment
    raise six.reraise(type(error), error, _stacktrace)
  File "/usr/local/lib/python3.5/dist-packages/urllib3/packages/six.py", line 685, in reraise
    raise value.with_traceback(tb)
  File "/usr/local/lib/python3.5/dist-packages/urllib3/connectionpool.py", line 600, in urlopen
    chunked=chunked)
  File "/usr/local/lib/python3.5/dist-packages/urllib3/connectionpool.py", line 384, in _make_request
    six.raise_from(e, None)
  File "<string>", line 2, in raise_from
  File "/usr/local/lib/python3.5/dist-packages/urllib3/connectionpool.py", line 380, in _make_request
    httplib_response = conn.getresponse()
  File "/usr/lib/python3.5/http/client.py", line 1197, in getresponse
    response.begin()
  File "/usr/lib/python3.5/http/client.py", line 297, in begin
    version, status, reason = self._read_status()
  File "/usr/lib/python3.5/http/client.py", line 266, in _read_status
    raise RemoteDisconnected("Remote end closed connection without"
urllib3.exceptions.ProtocolError: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response',))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "./monitor_system_os_reboot.py", line 67, in <module>
    FG.upload('system', 'os/reboot', data=UPLOAD_DATA)
  File "/usr/local/lib/python3.5/dist-packages/fortiosapi/fortiosapi.py", line 204, in upload
    data=data, files=files)
  File "/usr/local/lib/python3.5/dist-packages/requests/sessions.py", line 559, in post
    return self.request('POST', url, data=data, json=json, **kwargs)
  File "/usr/local/lib/python3.5/dist-packages/requests/sessions.py", line 512, in request
    resp = self.send(prep, **send_kwargs)
  File "/usr/local/lib/python3.5/dist-packages/requests/sessions.py", line 622, in send
    r = adapter.send(request, **kwargs)
  File "/usr/local/lib/python3.5/dist-packages/requests/adapters.py", line 495, in send
    raise ConnectionError(err, request=request)
requests.exceptions.ConnectionError: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response',))
'''
