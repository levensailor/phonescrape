import requests
import re
from bs4 import BeautifulSoup

class scrape:
    def allDetails(phone):
        details = {}
        headers = {}
        config_url = "http://"+phone+"/CGI/Java/Serviceability?adapter=device.statistics.configuration"
        device_url = "http://"+phone+"/CGI/Java/Serviceability?adapter=device.statistics.device"
        status_url = "http://"+phone+"/CGI/Java/Serviceability?adapter=device.settings.status.messages"

        try:
            config_response = requests.request("GET", config_url, headers=headers)
        except requests.exceptions.RequestException as e:  # This is the correct syntax
            return({})

        try:
            device_response = requests.request("GET", device_url, headers=headers)
        except requests.exceptions.RequestException as e:  # This is the correct syntax
            return({})

        try:
            status_response = requests.request("GET", status_url, headers=headers)
        except requests.exceptions.RequestException as e:  # This is the correct syntax
            return({})

        config_soup = BeautifulSoup(config_response.text, features="lxml")
        config_text = config_soup.get_text('_')

        device_soup = BeautifulSoup(device_response.text, features="lxml")
        device_text = device_soup.get_text('_')

        status_soup = BeautifulSoup(status_response.text, features="lxml")
        status_text = status_soup.get_text('_')

        '''
        These are found under the Device Information page
        '''

        res = re.search(r'(Serial number_|Serial Number_)([^_]*)', device_text)
        if res:
            details['sn'] = res.group(2).strip()
        res = re.search(r'(Version_)([^_]*)', device_text)
        if res:
            details['firmware'] = res.group(2).strip()
        res = re.search(r'(Phone DN_)([^_]*)', device_text)
        if res:
            details['dn'] = res.group(2).strip()
        res = re.search(r'(Model number_|Model Number_)([^_]*)', device_text)
        if res:
            details['model'] = res.group(2).strip()
        res = re.search(r'(Key expansion module 1_|Key Expansion Module 1_)([^_]*)', device_text)
        if res:
            details['kem1'] = res.group(2).strip()
        res = re.search(r'(Key expansion module 2_|Key Expansion Module 2_)([^_]*)', device_text)
        if res:
            details['kem2'] = res.group(2).strip()
        res = re.search(r'(MAC address_|MAC Address_)([^_]*)', config_text)
        if res:
            details['mac_address'] = res.group(2).strip()
        res = re.search(r'(Host name_|Host Name_)([^_]*)', config_text)
        if res:
            details['hostname'] = res.group(2).strip()
        res = re.search(r'(Domain name_|Domain Name_)([^_]*)', config_text)
        if res:
            details['domain_name'] = res.group(2).strip()
        res = re.search(r'(DHCP server_|DHCP Server_)([^_]*)', config_text)
        if res:
            details['dhcp_server'] = res.group(2).strip()
        res = re.search(r'(DHCP_)([^_]*)', config_text)
        if res:
            details['dhcp'] = res.group(2).strip()
        res = re.search(r'(IP address_|IP Address_)([^_]*)', config_text)
        if res:
            details['ip_address'] = res.group(2).strip()
        res = re.search(r'(Subnet mask_|Subnet Mask_)([^_]*)', config_text)
        if res:
            details['subnetmask'] = res.group(2).strip()
        res = re.search(r'(Default router_|Default Router 1_)([^_]*)', config_text)
        if res:
            details['gateway'] = res.group(2).strip()
        res = re.search(r'(DNS server 1_|DNS Server 1_)([^_]*)', config_text)
        if res:
            details['dns1'] = res.group(2).strip()
        res = re.search(r'(DNS server 2_|DNS Server 2_)([^_]*)', config_text)
        if res:
            details['dns2'] = res.group(2).strip()
        res = re.search(r'(Alternate TFTP_)([^_]*)', config_text)
        if res:
            details['alt_tftp'] = res.group(2).strip()
        res = re.search(r'(TFTP server 1_|TFTP Server 1)([^_]*)', config_text)
        if res:
            details['tftp1'] = res.group(2).strip()
        res = re.search(r'(TFTP server 2_)([^_]*)', config_text)
        if res:
            details['tftp2'] = res.group(2).strip()
        res = re.search(r'(Operational VLAN ID_|Operational VLAN Id_)([^_]*)', config_text)
        if res:
            details['op_vlan'] = res.group(2).strip()
        res = re.search(r'(Admin VLAN ID_|Admin VLAN Id_)([^_]*)',config_text)
        if res:
            details['admin_vlan'] = res.group(2).strip()       
        res = re.search(r'(CUCM server1_|Unified CM 1_)([^_]*)', config_text)
        if res:
            details['cucm1'] = res.group(2).strip()
        res = re.search(r'(CUCM server2_|Unified CM 2_)([^_]*)', config_text)
        if res:
            details['cucm2'] = res.group(2).strip()
        res = re.search(r'(CUCM server3_|Unified CM 3_)([^_]*)', config_text)
        if res:
            details['cucm3'] = res.group(2).strip()
        res = re.search(r'(Information URL_)([^_]*)', config_text)
        if res:
            details['info_url'] = res.group(2).strip()
        res = re.search(r'(Directories URL_)([^_]*)', config_text)
        if res:
            details['dir_url'] = res.group(2).strip()
        res = re.search(r'(Messages URL_)([^_]*)', config_text)
        if res:
            details['msg_url'] = res.group(2).strip()        
        res = re.search(r'(Services URL_)([^_]*)', config_text)
        if res:
            details['svc_url'] = res.group(2).strip()
        res = re.search(r'(Idle URL_)([^_]*)', config_text)
        if res:
            details['idle_url'] = res.group(2).strip()
        res = re.search(r'(Idle URL time_)([^_]*)', config_text)
        if res:
            details['info_url_time'] = res.group(2).strip()
        res = re.search(r'(Proxy Server URL_|Proxy server URL)([^_]*)', config_text)
        if res:
            details['proxy_url'] = res.group(2).strip()
        res = re.search(r'(Authentication URL_)([^_]*)', config_text)
        if res:
            details['auth_url'] = res.group(2).strip()
        res = re.search(r'(TVS_)([^_]*)', config_text)
        if res:
            details['tvs'] = res.group(2).strip()
        statuses = re.findall(r'(..:..:...m ..\/..\/...)(\n)([^_]*)', status_text)
        errors = []
        for status in statuses[-3:]:
            errors.append(status[0]+' '+status[2])
        details['status'] = errors
        return(details)
