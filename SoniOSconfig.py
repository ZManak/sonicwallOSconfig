import requests
import json


# Deshabilitar advertencias de certificados no verificados
requests.packages.urllib3.disable_warnings()


# Configuración básica
firewall_ip = "192.168.168.168"
username = "admin"
password = "your_password"
base_url = f"https://{firewall_ip}/api/sonicos/"


# Autenticación
def login():
    auth_url = base_url + "auth"
    payload = {"username": username, "password": password}
    response = requests.post(auth_url, json=payload, verify=False)
    if response.status_code == 200:
        return response.headers.get('X-Auth-Token')
    else:
        raise Exception(f"Error en autenticación: {response.text}")


# Configurar VPN Site-to-Site
def configure_vpn(auth_token):
    vpn_url = base_url + "vpn/policies/ipv4"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Auth-Token": auth_token
    }
    
    vpn_config = {
        "vpn": {
            "policies": {
                "ipv4": {
                    "policy": [
                        {
                            "name": "Site-to-Site-VPN",
                            "enabled": True,
                            "ike_id": {"type": "auto"},
                            "ike_gateway": {
                                "gateway_id": "1",
                                "local_gateway": {"interface": "X1"},
                                "peer_gateway": {"address": "203.0.113.10"}
                            },
                            "authentication": {
                                "method": "shared_secret",
                                "shared_secret": "YourStrongPreSharedKey123!"
                            },
                            "local_network": {"address_object": "LAN_SUBNET"},
                            "remote_network": {"address_object": "REMOTE_SUBNET"},
                            "proposal": {
                                "dh_group": "group14",
                                "encryption": "aes256",
                                "authentication": "sha256",
                                "lifetime": 28800
                            }
                        }
                    ]
                }
            }
        }
    }
    
    response = requests.post(vpn_url, headers=headers, json=vpn_config, verify=False)
    if response.status_code == 200:
        print("VPN configurada con éxito")
    else:
        print(f"Error configurando VPN: {response.text}")


# Flujo principal
try:
    auth_token = login()
    configure_vpn(auth_token)
    # Aquí puedes añadir más funciones para configurar firewall, SSL-VPN, etc.
except Exception as e:
    print(f"Error: {str(e)}")