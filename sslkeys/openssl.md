# How to create SSL/TLS Certificate and Keyfile

SSL is a termon commonly used for the same technology as TLS.

We need a SIGNED public key (=Certificate) for clients to encrypt and a privte key (=sslkey) for decrypting.

A certificate is a public key that is signed by a certificate authority (CA) which guarantees that this key belongs
to the person or organization that claims to be the owner.

The client will generate public and private keys automaticalls in the browser.

Here is the whole process how SSL/TLS works:

- Browser connects to server Using SSL (https)
- Server Responds with Server Certificate containing the public key of the web server.
- Browser verifies the certificate by checking the signature of the CA. To do this the CA certificate needs to be in the browser’s trusted store.
- If the signature is not in the store (Unknown) TLS still works, but you will get a unsecure connection warning from your browser.
- Browser uses this Public Key to agree a session key with the server.
- Web Browser and server encrypt data over the connection using the session key.

For production websites it's a good idea to get a certificate from a trusted CA for the domain of the website.
You can see the process [here](lets_encrypt.md).

For internal usages or development you could also use a so called selfsigned key.

With [openssl](https://www.openssl.org/) you can easily create a self signed SSL certificate and key.

[openssl Binaries](https://wiki.openssl.org/index.php/Binaries)

[Comprehensive Article regarding openssl topics](https://www.digitalocean.com/community/tutorials/openssl-essentials-working-with-ssl-certificates-private-keys-and-csrs)



### Configuration of openssl on Windows

- Download the prebuild binaries from the link above.
- Add Path to openssl to PATH.
- Add Environment variable OPENSSL_CONF to the openssl folder
- place the following openssl.conf file in the openssl folder

```
#
# Example OpenSSL configuration file for use with Let's Encrypt.
# This is only being used for generation of certificate requests.
# Modified from a standard example by Parliament Hill Computers Ltd.
#

# This definition stops the following lines choking if HOME isn't
# defined.
HOME			= .
RANDFILE		= .rnd

[ req ]
default_bits		= 2048
distinguished_name	= req_distinguished_name
attributes		    = req_attributes

# Stop confirmation prompts. All information is contained below.
prompt			    = no

# The extensions to add to a certificate request - see [ v3_req ]
req_extensions		= v3_req

[ req_distinguished_name ]
# Describe the Subject (ie the origanisation).
# The first 6 below could be shortened to: C ST L O OU CN
# The short names are what are shown when the certificate is displayed.
# Eg the details below would be shown as:
# Subject: C=UK, ST=Hertfordshire, L=My Town, O=Some Organisation, OU=Some Department, CN=www.example.com/emailAddress=bofh@example.com

# Leave as long names as it helps documentation
countryName=DE
stateOrProvinceName=NRW
localityName=YourCity
organizationName=YourOrganization
organizationalUnitName=Dev Server
commonName=www.your.domain.de
emailAddress=info@your.domain.de

[ req_attributes ]
# None. Could put Challenge Passwords, don't want them, leave empty

[ v3_req ]

# X509v3 extensions to add to a certificate request
# See x509v3_config

# What the key can/cannot be used for:
basicConstraints = CA:FALSE
keyUsage = nonRepudiation, digitalSignature, keyEncipherment
extendedKeyUsage = clientAuth,serverAuth

# The subjectAltName is where you give the names of extra web sites.
# You may have more than one of these, so put in the section [ alt_names ]
# If you do not have any extra names, comment the next line out.
subjectAltName = @alt_names

# List of all the other DNS names that the certificate should work for.
# alt_names is a name of my own invention
[ alt_names ]
DNS.1 = server1.your.domain.de
DNS.2 = server2.your.domain.de
DNS.3 = server3.your.domain.de 
DNS.4 = dev.your.domain.de

```
