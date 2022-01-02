from http.server import BaseHTTPRequestHandler, HTTPServer
import cgi

stackList = ['Microsoft Azure DevOps', 'Rust programming','OWASP Security Framework']
class Server(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.endswith('/'):
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            # self.wfile.write('Welcome to my python webserver'.encode())
            htmlOutput = ''
            htmlOutput += '<html><body>'
            htmlOutput += '<h1>Learning Stack Todo</h1>'
            htmlOutput += '<h3><a href ="/new">Add new stack</a></h3>'

            for stack in stackList:
                htmlOutput += stack
                htmlOutput += '</br>'

            htmlOutput += '</body></html>'
            self.wfile.write(htmlOutput.encode())

        if self.path.endswith('/new'):
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            htmlOutput = ''
            htmlOutput += '<html><body>'
            htmlOutput += '<h1>Add New Stack</h1>'
            htmlOutput += '<form method = "POST" enctype="multipart/form-data" action = "/new">'
            htmlOutput += '<input name="stack" type="text" placeholder= "Add a new stack">'
            htmlOutput += '<input type="submit" value="Add">'
            htmlOutput += '</form>'
            htmlOutput += '</body></html>'
            self.wfile.write(htmlOutput.encode())

    def do_POST(self):
        if self.path.endswith('/new'):
            ctype , pdict = cgi.parse_header(self.headers.get('content-type'))
            pdict['boundary'] = bytes(pdict['boundary'],"utf-8")
            content_len = int(self.headers.get('Content-length'))
            pdict['CONTENT_LENGTH'] = content_len
        

            if  ctype == 'multipart/form-data':
                fields = cgi.parse_multipart(self.rfile, pdict)
                new_stack = fields.get('stack')
                stackList.append(new_stack[0])

            self.send_response(301)
            self.send_header('content-type', 'text/html')
            self.send_header('location', '/')
            self.end_headers()


def main():
    hostName = "localhost"
    serverPort = 8080
    webServer = HTTPServer((hostName, serverPort), Server)
    print("Server started http://%s:%s" % (hostName, serverPort))
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")




if __name__ == "__main__": 
    main()      
