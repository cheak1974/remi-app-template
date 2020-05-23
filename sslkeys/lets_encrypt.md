
##Getting your SSL/TLS Certificate with Let's Encrypt for free

- edit your DNS setting that the domain is pointing to your servers static IP
- disable all services listening on port 80
- open port 80 in firewall settings of your server
- install cert bot
- If all went well the certificates are stored in /etc/letsencrypt/keys
- point to the keyfiles with /config/config.py
- enable remi app template again
- if existing configure your reverse proxy to redirect http to https

```python
</location_of_remi_app_template/config/config.py>
core.globals.config['rel_path_to_ssl_certfile'] = sys.path[0] + '/sslkeys/fullchain.pem'
core.globals.config['rel_path_to_ssl_keyfile'] = sys.path[0] + '/sslkeys/privkey.pem'
```

Or you can keep the original location of the keyfiles by entering:

```
</location_of_remi_app_template/config/config.py>
core.globals.config['rel_path_to_ssl_certfile'] = '/etc/letsencrypt/keys/fullchain.pem'
core.globals.config['rel_path_to_ssl_keyfile'] = '/etc/letsencrypt/keys/sslkeys/privkey.pem'
```