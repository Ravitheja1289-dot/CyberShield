import requests

# Replace with your actual API key
API_KEY = "402132554c33a11133e7ea1a8bbceb74a5eadb87087dc89eaab12b18f339027e"

# Function to scan a URL
def scan_url(url):
    vt_url = "https://www.virustotal.com/api/v3/urls"
    headers = {"x-apikey": API_KEY}
    
    # Encoding URL
    data = {"url": url}
    response = requests.post(vt_url, headers=headers, data=data)
    
    if response.status_code == 200:
        scan_id = response.json()["data"]["id"]
        print(f"Scan submitted successfully! Scan ID: {scan_id}")
        return scan_id
    else:
        print("Error:", response.json())
        return None

# Function to get scan results
def get_scan_report(scan_id):
    vt_url = f"https://www.virustotal.com/api/v3/analyses/{scan_id}"
    headers = {"x-apikey": API_KEY}
    
    response = requests.get(vt_url, headers=headers)
    
    if response.status_code == 200:
        result = response.json()
        stats = result["data"]["attributes"]["stats"]
        print(f"Scan Report:\n {stats}")
    else:
        print("Error:", response.json())

# Example usage
sample_url = "http://example.com/malware"
scan_id = scan_url(sample_url)

if scan_id:
    print("\nFetching scan report...\n")
    get_scan_report(scan_id)