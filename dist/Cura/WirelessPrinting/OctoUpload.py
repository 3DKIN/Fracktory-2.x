#Param: uploadBool(string:yes) Upload gcode after slice
#Param: hostIP(string:octopi.local) IP Address
#Param: octoPort(string:80) Port
#Param: apiKey(string:) API Key
#Param: outputName(string:output) Output Filename
#Param: sendLoc(string:local) OctoPrint Location (local or sdcard)
#Param: gcodeExt(string:gcode) GCode Extension
#Param: sslBool(string:no) SSL (yes/no)
#Param: selectBool(string:yes) Select once uploaded (yes/no)
#Param: printBool(string:no) Print after upload (yes/no)

version = "0.1"

import base64
# import socket
import urllib
import urllib2
import mimetools
import sys
import os

# timeout = 15
# socket.setdefaulttimeout(timeout)

# #remove extension user may have used on the filename
# outputName = outputName.split(".")[0]
# print outputName

# #remove . user may have used on extension
# if gcodeExt.find(".") != -1:
#     gcodeExt = gcodeExt.split(".")[1]
#     print gcodeExt
#
# #add extension user specifies
# if gcodeExt == "g":
#     outputName = outputName + "." + gcodeExt
# elif gcodeExt == "gco":
#     outputName = outputName + "." + gcodeExt
# else:
#     outputName = outputName + ".gcode"
# print "Ext: " + outputName


# username = "spec"
# password = "password"


#allows for SSL if user specifies

def start_upload_file(hostIP,octoPort,api_key,sendLoc,printBool,filename):
    protocol = "http://"

    #sends the gcode to either sd or local
    if sendLoc == "sdcard":
        url = protocol + hostIP + ":" + octoPort + "/api/files/sdcard"
    else:
        url = protocol + hostIP + ":" + octoPort + "/api/files/local"

    if printBool == "yes":
        selectBool = "yes"
    elif printBool == "no":
        selectBool = "no"

    #makes sure user submits a valid option for printing
    if printBool != ("yes" or "no"):
        selectBool = "no"
        printBool = "no"


    try:
        # Upload png 
        filebody = open(filename.replace(".gcode", ".png"), 'rb').read()
        mimetype = 'application/octet-stream'
        boundary = mimetools.choose_boundary()
        content_type = 'multipart/form-data; boundary=%s' % boundary

        outputName = os.path.basename(filename)
        body = []
        body_boundary = '--' + boundary
        body = [  body_boundary,
                'Content-Disposition: form-data; name="file"; filename="%s"' % outputName,
                'Content-Type: %s' % mimetype,
                '',
                filebody,
                '--' + boundary,
                'Content-Disposition: form-data; name="select"',
                '',
                "no",
                '--' + boundary,
                'Content-Disposition: form-data; name="print"',
                '',
                "no",
                ]

        body.append('--' + boundary + '--')
        body.append('')
        body = '\r\n'.join(body)

        req = urllib2.Request(url)
        req.add_header('User-agent', 'Fracktory AutoUploader')
        req.add_header('Content-type', content_type)
        req.add_header('Content-length', len(body))
        req.add_header('X-Api-Key', api_key)
        req.add_data(body)

        print "Uploading...png"
        print urllib2.urlopen(req).read()
        print "Done"
        
    except Exception as e:
        print e

    filebody = open(filename, 'rb').read()
    mimetype = 'application/octet-stream'
    boundary = mimetools.choose_boundary()
    content_type = 'multipart/form-data; boundary=%s' % boundary

    outputName = os.path.basename(filename)
    body = []
    body_boundary = '--' + boundary
    body = [  body_boundary,
            'Content-Disposition: form-data; name="file"; filename="%s"' % outputName,
            'Content-Type: %s' % mimetype,
            '',
            filebody,
            '--' + boundary,
            'Content-Disposition: form-data; name="select"',
            '',
            selectBool,
            '--' + boundary,
            'Content-Disposition: form-data; name="print"',
            '',
            printBool,
            ]

    body.append('--' + boundary + '--')
    body.append('')
    body = '\r\n'.join(body)

    req = urllib2.Request(url)
    req.add_header('User-agent', 'Fracktory AutoUploader')
    req.add_header('Content-type', content_type)
    req.add_header('Content-length', len(body))
    req.add_header('X-Api-Key', api_key)
    req.add_data(body)

    print "Uploading...gcode"
    print urllib2.urlopen(req).read()
    print "Done"

