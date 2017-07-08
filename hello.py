from flask import Flask
from werkzeug.contrib.fixers import ProxyFix
app = Flask(__name__)

def wsgi_application(environ,start_response):
    status = '200 OK'
    headers = [
        ('Content-Type', 'text/plain')
    ]
    body = [bytes(i + '\n', 'ascii') for i in environ['QUERY_STRING'].split('&')]
    start_response(status, headers)
    return body

app.wsgi_application = ProxyFix(app.wsgi_application)
if __name__ == '__main__':
    app.run()
