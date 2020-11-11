[![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/levensailor/phonescrape)

# phonescrape

Uses BeautifulSoup and RegEx to pull and parse data directly form Cisco IP Phones

```bash
pip install phonescrape
```

#### input a phone ip address

```py
from phonescrape import scrape

phones = ['10.131.202.127', '10.131.202.127']

for phone in phones:
    details = scrape.allDetails(phone)
    print(details["sn"])

FCH2053D2BS

```

#### and get back a dict of information:

```json
{
    "sn": "FCH2053D2BS",
    "firmware": "sip88xx.12-0-1-8",
    "dn": "52807",
    "model": "CP-8851",
    "kem1": "Key expansion module 2",
    "kem2": "Hardware revision",
    "mac_address": "F8A5C59E0F1C",
    "hostname": "SEPF8A5C59E0F1C",
    "domain_name": "DHCP server",
    "dhcp_server": "10.131.202.1",
    "dhcp": "Yes",
    "ip_address": "10.131.202.127",
    "subnetmask": "255.255.255.0",
    "gateway": "10.131.202.1",
    "dns1": "8.8.8.8",
    "dns2": "DNS server 3",
    "alt_tftp": "Yes",
    "tftp1": "10.144.200.10",
    "tftp2": "DHCP address released",
    "op_vlan": "Admin VLAN ID",
    "admin_vlan": "CUCM server1",
    "cucm1": "10.144.200.10  Active",
    "cucm2": "",
    "cucm3": "CUCM server4",
    "info_url": "http://10.144.200.10:8443/ccmcip/GetTelecasterHelpText.jsp",
    "dir_url": "http://10.144.200.10:8443/ccmcip/xmldirectory.jsp",
    "msg_url": "Services URL",
    "svc_url": "http://10.144.200.10:8443/ccmcip/getservicesmenu.jsp",
    "idle_url": "Idle URL time",
    "info_url_time": "0",
    "proxy_url": "",
    "auth_url": "http://10.144.200.10:8080/ccmcip/authenticate.jsp",
    "tvs": "cucm.car.pnslabs.com",
    "status": [
        "11:39:03am 10/09/18 ITL installed",
        "11:39:04am 10/09/18 SEPF8A5C59E0F1C.cnf.xml.sgn(HTTP)",
        "11:39:05am 10/09/18 VPN not configured"
    ]
}
```
