from http.server import SimpleHTTPRequestHandler, HTTPServer 

 

PORT = 8080 

Handler = SimpleHTTPRequestHandler 

 

with HTTPServer(("", PORT), Handler) as httpd: 

    print("Serving at port", PORT) 

    httpd.serve_forever() 