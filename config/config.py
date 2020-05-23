import sys
import ssl
import core.globals
import models.customer

# This file is imported at App start and overwrites standard values in core/globals.py with user specific values
# You can also place your secret API keys etc. here (you should take out this file from Version Control with .gitignore in this case)

core.globals.config['appname'] = 'REMI Template App'
core.globals.config['author'] = 'Christian Kueken'
core.globals.config['version'] = 'V1.0'
core.globals.config['standalone'] = False
core.globals.config['multiple_instance'] = True
core.globals.config['port'] = 8080
core.globals.config['address'] = '0.0.0.0'
core.globals.config['start_browser'] = False
core.globals.config['debug'] = False
core.globals.config['enable_file_cache'] = False
core.globals.config['update_interval'] = 0.1
core.globals.config['base_padding'] = 10
core.globals.config['navbar_height'] = 30
core.globals.config['is_behind_proxy'] = False          # Try to get the original host IP from Header information because host is always the proxy

# SSL Configuration (uncomment lines if you want to use SSL/TLS)
#core.globals.config['rel_path_to_ssl_certfile'] = sys.path[0] + '//sslkeys//fullchain.pem'         # Create with openssl or via CA
#core.globals.config['rel_path_to_ssl_keyfile'] = sys.path[0] + '//sslkeys//privkey.pem'          # Create with openssl or via CA
#core.globals.config['use_ssl_version'] = ssl.PROTOCOL_TLS


# mongo DB Database Data


# Custom Headdata to be added to the Application

core.globals.config['headdata'] = """
                        <meta name="viewport" content="width=device-width, initial-scale=1">
                        <meta name="description" content="REMI App Template">
                        <meta name="author" content="Christian Kueken">

                        <link rel="stylesheet" href="/static:css/w3/w3.css">

                        <link rel="stylesheet" href="/static:css/fa/css/all.css" >
                        <script defer src="/static:css/fa/js/all.js"></script>

                        <link rel="stylesheet" href="/static:css/bootstrap4/css/bootstrap.min.css" >
                        <script src="/static:css/bootstrap4/js/bootstrap.min.js"></script>
                        <script src = "/static:js/jquery/jquery-3.4.1.slim.js"></script>
                        <script src = "/static:js/popper/popper.min.js"></script>
                        <script src = "/static:js/popper/tooltip.min.js"></script>

                        <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto|Roboto+Condensed|Lobster|Tangerine">

                        <title>REMI App</title>

                        <style> 
                        html, body {padding: 0; margin: 0; height: 100%;}
                        .w3-roboto {font-family: "Roboto", serif; }
                        .w3-roboto-cond {font-family: "Roboto Condensed", serif; }
                        .w3-lobster {font-family: "Lobster", serif; font-size: 14px; text-shadow: none;}
                        .w3-tangerine {font-family: "Tangerine", serif; font-size: 24px; text-shadow: 3px 3px 3px #aaa;}
                        </style>
                        """

# Add User Data for the Application
# core/globals.py defines a Dict UserData for storing User specific Data that should be available everywhere
# You could also write an own module and use a database or whatever you need
core.globals.UserData['sample1'] = models.customer.Customer(firstname='Christian', lastname='Kueken', city='Kaarst')
core.globals.UserData['sample2'] = models.customer.Customer(firstname='Davide', lastname='Rosa', city='Venice')
