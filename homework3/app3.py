def app(environ, start_response):
    data = b"Hello, Nikita!\n"
    headers = [("Content-Type", "text/plain"),
            ("Content-Length", str(len(data)))]
    start_response("200 OK", headers)
    return iter([data])