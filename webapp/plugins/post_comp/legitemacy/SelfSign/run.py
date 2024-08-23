import os
import subprocess

def desc():
    return "Self Signing Certificate"

def run():
    PASSWORD       = "verysecuresecretpassword"
    openssl_config = '''
[req]
prompt = no
distinguished_name = dn
x509_extensions = x509_ext

[dn]
CN = maldev.com
emailAddress = evil@maldev.com
O = Maldev
L = New York Cit
ST = New York
C = EU

[x509_ext]
basicConstraints = CA:FALSE
subjectKeyIdentifier = hash
authorityKeyIdentifier = keyid,issuer
'''

    # Write openssl config to file
    with open('openssl.cnf', 'w') as f:
        f.write(openssl_config)

    subprocess.run(f"openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -sha256 -days 365 -nodes -config openssl.cnf", shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    subprocess.run(f"openssl pkcs12 -export -in cert.pem -inkey key.pem -passin pass:{PASSWORD} -out sign.pfx -passout pass:{PASSWORD}", shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    subprocess.run(f"osslsigncode sign -pkcs12 sign.pfx -in result.exe -out result_sign.exe -pass {PASSWORD}", shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # Move signed executable to result.exe
    os.replace("result_sign.exe", "result.exe")

    return