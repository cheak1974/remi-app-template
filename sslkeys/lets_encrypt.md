
##Getting your SSL/TLS Certificate with Let's Encrypt for free

[Let's Encrypt](https://letsencrypt.org/)

- edit your DNS setting that the domain is pointing to your servers static IP
- disable all services listening on port 80
- open port 80 in firewall settings of your server
- ssh login to your server
- Install certbot
```shell script
sudo apt-get update
sudo apt-get install software-properties-common
sudo add-apt-repository universe
sudo apt-get update
sudo apt-get install certbot
```
- Let certbot do it's job :-) (Remember that Remi App Template has to switched off)
```shell script
sudo certbot certonly --standalone
```
- If all went well the certificates are stored in /etc/letsencrypt/keys
- point to the keyfiles with /config/config.py
- enable remi app template again
- if existing configure your reverse proxy to redirect http to https

You can copy the freshly created keys from /etc/letsencrypt/live/your.domain.com/ to REMI App Template sslkeys folder

```python
</location_of_remi_app_template/config/config.py>
core.globals.config['rel_path_to_ssl_certfile'] = sys.path[0] + '/sslkeys/fullchain.pem'
core.globals.config['rel_path_to_ssl_keyfile'] = sys.path[0] + '/sslkeys/privkey.pem'
```

or you can keep the original location of the keyfiles by entering:

```
</location_of_remi_app_template/config/config.py>
core.globals.config['rel_path_to_ssl_certfile'] = '/etc/letsencrypt/live/your.domain.com/fullchain.pem'
core.globals.config['rel_path_to_ssl_keyfile'] = '/etc/letsencrypt/live/your.domain.com/privkey.pem'
```