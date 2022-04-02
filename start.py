#! /usr/bin/env python

import webbrowser
import SimpleHTTPServer
import SocketServer

port =1585 

print "starting web browser"
webbrowser.open("http://localhost:%d" % port, new=2)

print "serving http://localhost:%d" % port
httpd = SocketServer.TCPServer(("", port), SimpleHTTPServer.SimpleHTTPRequestHandler)
httpd.serve_forever()

