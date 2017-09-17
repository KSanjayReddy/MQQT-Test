import webbrowser
from skpy import Skype


username="sripad1996@gmail.com"
password="dapirs1996"
sk = Skype(username, password)

webbrowser.open('https://login.skype.com/login?client_id=578134&redirect_uri=https%3A%2F%2Fweb.skype.com')
