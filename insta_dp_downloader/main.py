"""
Author: https://github.com/wasim-shakir5
"""

import instaloader

def downloadInstaDp(username):
    loader = instaloader.Instaloader()
    
    try:
        loader.download_profile(username, profile_pic_only=True)
        print(f"Profile picture of {username} downloaded successfully.")
    except instaloader.exceptions.ProfileNotExistsException:
        print(f"Profile with username '{username}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    username = input("Enter Instagram username: ")
    downloadInstaDp(username)
