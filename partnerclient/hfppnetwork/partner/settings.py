# -*- coding: utf-8 -*-
"""
Copyright (C) 2013 TopCoder Inc., All Rights Reserved.

This is the module that defines the settings(configurations) of the Partner Client.
It defines a set of configuration parameters.
This module resides in Python source file settings.py
Thread Safety:
No thread safety concern here because this module doesn't define any functions.
@author: TCSASSEMBLER
@version: 1.0
"""
"""
Represents the base URL of HFPP Network Node HTTP Services.
It should be non-None/empty str.
Required.
"""
HFPP_NODE_HTTP_SERVICE_BASE_URL = 'https://ec2-184-72-145-164.compute-1.amazonaws.com/NetworkNode1/services'
"""
Represents the CA certificate file path used
as the SSL certificate for accessing HFPP Network Node HTTP Services via HTTPS.
It should be non-None/empty str.
Required.
"""
CA_CERTIFICATE_FILE = '/usr/local/tomcat/conf/cert.cer'
"""
Represents the CA certificate file path used by this partner server.
It should be non-None/empty str.
Required.
"""
PARTNER_CERTIFICATE = '/usr/local/tomcat/conf/cert.cer'
"""
Represents the SSL key file path used by this partner server.
It should be non-None/empty str.
Required.
"""
PARTNER_PRIVATE_KEY = '/usr/local/tomcat/conf/unsec_server.key'
"""
Represents the HFPP Network Partner ID of this partner client.
It should be non-None/empty str. It is supposed to be a UUID.
Required.
"""
HFPP_PARTNER_ID = '091f80d7-8ecb-429c-8f0b-caeaae18dcd8'
"""
Represents the HFPP Network username of this partner client.
It should be non-None/empty str.
Required
"""
HFPP_PARTNER_USERNAME = 'user1'
"""
Represents the HFPP Network password of this partner client.
It should be non-None/empty str.
Required.
"""
HFPP_PARTNER_PASSWORD = 'pass1'
"""
Represents the HFPP Network port of this partner client.
It should be an integer in range [0, 65535]
Required.
"""
PARTNER_CLIENT_HTTP_SERVICE_PORT = 8071
"""
Represents the comming request should be immediately responded or approved by administrator.
It should be an boolean value.
Required.
"""
PARTNER_IMMEDIATE_FULLFIL = True
"""
Represents the URL of decision module.
It should be non-None/empty str.
Required.
"""
DECISION_MODULE_URL = 'http://localhost:8001/create'

"""
The directory to save the study report files.
String.
Required.
"""
STUDY_REPORT_DIRECTORY = "../../study"
