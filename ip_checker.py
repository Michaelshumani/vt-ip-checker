import requests
import os

API_KEY = os.environ.get("VT_API_KEY")

def check_ip(ip_address):
    url = f"https://www.virustotal.com/api/v3/ip_addresses/{ip_address}"
    headers = {"x-apikey": API_KEY}

    print(f"\nChecking VirusTotal for: {ip_address}")
    print("-" * 40)

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"Error: {response.status_code} - Could not retrieve data")
        return

    data = response.json()
    stats = data["data"]["attributes"]["last_analysis_stats"]

    malicious  = stats["malicious"]
    suspicious = stats["suspicious"]
    clean      = stats["undetected"]
    community  = data["data"]["attributes"]["reputation"]

    print(f"Malicious  : {malicious} engines")
    print(f"Suspicious : {suspicious} engines")
    print(f"Clean      : {clean} engines")
    print(f"Community  : {community}")
    print("-" * 40)

    if malicious >= 5:
        print("VERDICT: WARNING - MALICIOUS - Block this IP immediately")
    elif suspicious >= 3 or malicious >= 1:
        print("VERDICT: WARNING - SUSPICIOUS - Investigate further")
    else:
        print("VERDICT: CLEAN - No threats detected")

ip = input("\nEnter IP address to check: ")
check_ip(ip)
