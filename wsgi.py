def app(environ, start_response):
    data=b'Hello\n'
    status='200 OK'
    response_headers=[
    ('Content-type', 'text/plain'),
    ('Content-length', str(len(data)))
    ]
    start_response(status, response_headers)
    return iter([data])