# VT IP Checker

A Python tool that checks an IP address against VirusTotal and returns a threat verdict.

## What it does
- Queries the VirusTotal API v3
- Returns malicious, suspicious, and clean engine counts
- Gives a clear verdict: MALICIOUS, SUSPICIOUS, or CLEAN

## Tools Used
- Python 3
- VirusTotal API v3
- requests library

## How to Run
1. Set your VirusTotal API key as an environment variable:
   $env:VT_API_KEY = "your-key-here"

2. Run the script:
   py ip_checker.py

3. Enter any IP address when prompted

## Example Output
Checking VirusTotal for: 185.220.101.45
----------------------------------------
Malicious  : 17 engines
Suspicious : 2 engines
Clean      : 29 engines
Community  : -21
----------------------------------------
VERDICT: WARNING - MALICIOUS - Block this IP immediately

## Author
Shumani Michael Bologo
Service Desk Analyst | Cloud Administrator | AZ-900 | SC-900
