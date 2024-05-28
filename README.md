# VRChat Group Member Scraper

This script uses the VRChat API to export a text file containing every member of a specified VRChat group.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Finding Group ID and Auth Tokens](#finding-group-id-and-auth-tokens)
- [License](LICENSE)
- [Example](#example)

## Installation

1. Download the export_members.py script from the repository.

2. Install the required Python packages:
    ```bash
    pip install requests
    ```

## Usage

1. Open the `export_members.py` file and update the following variables with your group ID and authentication tokens:
    ```python
    group_size = 1000  # Set to the total number of members in the group
    group_id = "GROUP_ID_HERE"
    cookies = {
        'auth': 'YOUR_AUTH_TOKEN_HERE',
        'twoFactorAuth': 'YOUR_2FA_TOKEN_HERE'
    }
    ```

2. Run the script:
    ```bash
    python export_members.py
    ```

3. After the script completes, you will find a file named `members.txt` containing the list of group members.

## Finding Group ID and Auth Tokens

1. **Finding the Group ID**:
    - Navigate to your VRChat group page.
    - Copy the string after `group/` in the URL. This is your `group_id`.
    - Ex: grp_b75c5810-6df2-4f88-9365-41dc30522378

2. **Finding Auth Tokens**:
    - Go to any VRChat group page and navigate to the members list.
    - Right-click and select `Inspect Element` to open the developer tools.
    - Go to the `Network` tab, then scroll down the group members list and press the `Load More Members` button.
    - In the `Network` tab, on the left side, look for a network request named `members?n=25&offset=25` with an orange semicolon in brackets icon.
    - Click on it and find the `Cookies` section on the right panel.
    - Copy the `auth` token and `twoFactorAuth` token from the cookies section into your script.

3. **Setting Group Size**:
    - Set the `group_size` variable to the total number of members in the group.

## Example

Here's an example of how to set up the script:
```python
group_size = 16234  # Total number of members in the group
group_id = "grp_b75c5810-6df2-4f88-9365-41dc30522378"
cookies = {
    'auth': 'authcookie_9a87b6c5-4321-4f12-8765-abcde12345fg',
    'twoFactorAuth': 'eyJhhGciOnFIUzI1NfAsInR5cCI6IgpXVCJ9.eyJ1c2VjSWQiOiJ1c3JfOWFhYWEyMy00NTYzLTRmMTItODc2NS1hYmNkZTEyMzQ1ZmciLCJtYWNBY2Nlc3MiOiIiLCJ0aW1lc3RhbXAiOjE2MzEyMjM4NjAwNTQsInZlcnNpb24iOjIsImlhdCI6MTYzMTIyMzg2MCwiZXhwIjoxNjMxMjI0MjYwfQ.QwertyUiOpAsDfGhjKlZxCvBnMkQwErTyUiOpAsDfGhjKlZxCvBnMkQwEr'
}
```

## Tip

If you are trying to find a specific player in a group
- Simply Crtl + F their name in the exported file
- Then copy their User ID
- Then replace THEIR_USER_ID with the User ID you just copied https://vrchat.com/home/user/THEIR_USER_ID
- The result should be the link to that specific user's profile
