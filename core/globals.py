import remi

config = {}

config['appname'] = 'REMI Template App'
config['author'] = 'Christian Kueken'
config['version'] = '1.0'
config['standalone'] = False
config['multiple_instance'] = True
config['port'] = 8080
config['address'] = '0.0.0.0'
config['start_browser'] = False
config['debug'] = False
config['enable_file_cache'] = False
config['update_interval'] = 0.1
config['rel_path_to_static'] = '//static'
config['base_padding'] = 10
config['navbar_height'] = 25
config['reconnect_timeout'] = 30.0


# SSL Configuration of REMI
config['rel_path_to_ssl_certfile'] = ''
config['rel_path_to_ssl_keyfile'] = ''
config['use_ssl_version'] = None



config['headdata'] = """
                        <meta name="viewport" content="width=device-width, initial-scale=1">
                        <meta name="description" content="SmarterHouses">
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

UserData = {}
