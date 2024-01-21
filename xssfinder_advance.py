import requests
import subprocess

def get_filtered_urls(target_url):
    """Retrieves URLs from waybackurls, filters for potential XSS targets, and handles errors."""
    try:
        cmd = f"waybackurls {target_url}"
        result = subprocess.run(cmd.split(), capture_output=True, text=True)  # Avoid shell=True
        urls = [line for line in result.stdout.splitlines() if "=" in line]
        return urls
    except subprocess.CalledProcessError as e:
        print(f"Error running waybackurls: {e}")
        return []

def test_for_xss(urls, payload):
    """Tests URLs for XSS vulnerabilities and handles errors."""
    for url in urls:
        try:
            response = requests.get(url.replace("=", f'=">{payload}'))
            if payload in response.text:
                print("XSS found:", url)
            else:
                print("XSS not found:", url)
        except requests.exceptions.RequestException as e:
            print(f"Error fetching URL: {e}")

def main():
    """Prompts for target URL and payload, calls necessary functions, and ensures proper execution."""
    target_url = input("Enter target URL: ")
    payload = input("Enter payload: ")

    urls = get_filtered_urls(target_url)
    if urls:
        test_for_xss(urls, payload)
    else:
        print("No URLs retrieved from waybackurls.")

if __name__ == "__main__":
    main()
