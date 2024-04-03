import sys
import requests
import warnings

def check_endpoint(url, endpoint):
    full_url = url + endpoint.strip()
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
        "Host": full_url.split('/')[2],
        "Connection": "Keep-alive"
    }
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            response = requests.get(full_url, headers=headers, verify=False)
        if response.status_code == 200:
            return endpoint.strip()  # Return the endpoint if accessible
        else:
            return None
    except Exception as e:
        return None

def main():
    if len(sys.argv) != 5 or sys.argv[1] != '-u' or sys.argv[3] != '-w':
        print("Usage: python actuator.py -u <URL> -w <wordlist.txt>")
        return

    url = sys.argv[2]
    if not url.startswith("http"):
        url = "https://" + url

    wordlist_file = sys.argv[4]
    try:
        with open(wordlist_file, 'r') as f:
            wordlist = f.readlines()
    except FileNotFoundError:
        print(f"Error: {wordlist_file} not found.")
        return

    accessible_endpoints = []
    for word in wordlist:
        endpoint = "/actuator/" + word.strip()
        result = check_endpoint(url, endpoint)
        if result:
            accessible_endpoints.append(result)

    if accessible_endpoints:
        print("Accessible endpoints:")
        for endpoint in accessible_endpoints:
            print(endpoint)
    else:
        print("No accessible endpoints found.")

if __name__ == "__main__":
    main()
