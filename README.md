# VT IP Checker

A Python automation tool that checks an IP address against VirusTotal and returns a threat verdict. Built as a cybersecurity portfolio project.

## What it does
- Queries the VirusTotal API v3
- Checks against 70+ antivirus and threat intelligence engines
- Returns malicious, suspicious, and clean engine counts
- Gives a clear verdict: MALICIOUS, SUSPICIOUS, or CLEAN
- Uses environment variables to keep API keys secure

## Architecture

![Architecture](architecture-diagram.png)

![Flow](flow-diagram.png)
User inputs IP ? Python script loads API key from environment ? Sends HTTPS request to VirusTotal API v3 ? 70+ engines analyse the IP ? JSON response parsed ? Verdict printed to terminal

## Flow
1. Run the script
2. Enter any IP address
3. Script calls VirusTotal API securely
4. Parses JSON response
5. Returns verdict: MALICIOUS / SUSPICIOUS / CLEAN

## Tools Used
- Python 3
- VirusTotal API v3
- requests library
- Environment variables for secret management

## How to Run
1. Get a free API key at virustotal.com
2. Set your key as an environment variable:
   $env:VT_API_KEY = "your-key-here"
3. Run the script:
   py ip_checker.py
4. Enter any IP address when prompted

## Example Output
Checking VirusTotal for: 185.220.101.45
----------------------------------------
Malicious  : 17 engines
Suspicious : 2 engines
Clean      : 29 engines
Community  : -21
----------------------------------------
VERDICT: WARNING - MALICIOUS - Block this IP immediately

Checking VirusTotal for: 8.8.8.8
----------------------------------------
Malicious  : 0 engines
Suspicious : 0 engines
Clean      : 35 engines
Community  : 539
----------------------------------------
VERDICT: CLEAN - No threats detected

## Security Note
Never hardcode your API key. Always use environment variables.
This project uses os.environ.get() to keep credentials out of code.

## Author
Shumani Michael Bologo
Service Desk Analyst | Cloud Administrator Trainee
AZ-900 | SC-900 | AZ-104 In Progress
github.com/Michaelshumani
