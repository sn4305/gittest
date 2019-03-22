import urllib.request
import ftplib
url = 'https://www.ipc.org/4.0_Knowledge/4.1_Standards/IPC-A-610E-redline-April-2010.pdf'
Host = "4305.pro:2221"
# Port = '1222'
User = 'root'
Passwd = 'yangdong'

response = urllib.request.urlopen(url)
html = response.read()
#html = html.encode("utf-8")
f = open(".pdf","wb")
f.write(html)
f.close()


