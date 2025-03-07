from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Replace with your actual API key
API_KEY = "402132554c33a11133e7ea1a8bbceb74a5eadb87087dc89eaab12b18f339027e"

# Function to scan a URL
def scan_url(url):
    vt_url = "https://www.virustotal.com/api/v3/urls"
    headers = {"x-apikey": API_KEY}
    data = {"url": url}

    response = requests.post(vt_url, headers=headers, data=data)

    if response.status_code == 200:
        scan_id = response.json()["data"]["id"]
        return scan_id
    else:
        return None

# Function to get scan results
def get_scan_report(scan_id):
    vt_url = f"https://www.virustotal.com/api/v3/analyses/{scan_id}"
    headers = {"x-apikey": API_KEY}

    response = requests.get(vt_url, headers=headers)

    if response.status_code == 200:
        result = response.json()
        stats = result["data"]["attributes"]["stats"]
        return stats
    else:
        return None

# Flask API Route
@app.route("/scan", methods=["POST"])
def scan():
    data = request.json
    url = data.get("url")

    if not url:
        return jsonify({"error": "No URL provided"}), 400

    scan_id = scan_url(url)
    if scan_id:
        report = get_scan_report(scan_id)
        return jsonify({"scan_id": scan_id, "report": report})
    else:
        return jsonify({"error": "Failed to scan URL"}), 500

if __name__ == "__main__":
    app.run(debug=True)
