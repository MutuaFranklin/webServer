# WebServer


### Description

A web server that can support only a restricted subset of HTTP, such as GET or POST requests, and the only headers it must support are Content-Type and Content-Length.

### Author

**Franklin Mutua** - [Github link](https://github.com/MutuaFranklin/)

### Date of current version

02/01/2022


## Technologies Used
- Python
- OpenSSL 

### Installing

When you create a repository on GitHub, it exists as a remote repository. You can clone your repository to create a local copy on your computer and sync between the two locations. Here is a series of steps on how to set up the project on your local machine.

Click [webServer](https://github.com/MutuaFranklin/webServer) to navigate on the main page of the project repository on Github.

```
Clone the repository using HTTPS, click "Clone with HTTPS".
```

```
Open Terminal. Change the current working directory to the location where you want the cloned directory.
```

```
Type https://github.com/MutuaFranklin/webServer and press Enter to create your local clone.

```
```
Run 'openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -days 365' command in your terminal to generate key and cert files with OpenSSL

```

```
Open webServer, the cloned Repo in terminal and run :python webserver1.py  and enter PEM pass phrase to launch using socketserver.TCPServer and python webserver2.py to launch using HTTPServer


```

### BDD
- serve both static HTML and dynamically generated HTML 
- support only a restricted subset of HTTP, such as GET or POST requests
- only headers it must support are Content-Type and Content-Length.


