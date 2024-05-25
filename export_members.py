import requests
import time

# Define the group size, id, and your auth tokens
# Example Group ID: grp_b75c5810-6df2-4f88-9365-41dc30522378
# See README.MD on how to find group id and auth tokens
group_size = 1000 # Set to the total number of members in the group
group_id = "GROUP_ID_HERE"
cookies = {
    'auth': 'YOUR_AUTH_TOKEN_HERE',
    'twoFactorAuth': 'YOUR_2FA_TOKEN_HERE'
}

# DONT CHANGE BELOW HERE
headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": f"https://vrchat.com/home/group/{group_id}/members",
    "Sec-Ch-Ua": '"Opera GX";v="109", "Not:A-Brand";v="8", "Chromium";v="123"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"Windows"',
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 OPR/109.0.0.0"
}
base_url = f"https://vrchat.com/api/1/groups/{group_id}/members"
batch_size = 100
with open("members.txt", "w", encoding="utf-8") as file:
    for offset in range(0, group_size, batch_size):
        url = f"{base_url}?n={batch_size}&offset={offset}"
        response = requests.get(url, headers=headers, cookies=cookies)
        if response.status_code == 200:
            data = response.json()
            for item in data:
                user_id = item.get('userId')
                display_name = item.get('user', {}).get('displayName')
                thumbnail_url = item.get('user', {}).get('thumbnailUrl')
                file.write(f"User ID: {user_id}, Display Name: {display_name}, Thumbnail URL: {thumbnail_url}\n")
            print(f"{offset + batch_size} / {group_size} members written to members.txt.")
        else:
            print(f"Request failed with status code: {response.status_code} at offset {offset}")
        # Delay between requests to avoid overwhelming the server
        time.sleep(1)

print("All user information has been written to file.")
