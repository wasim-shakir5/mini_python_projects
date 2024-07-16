# Instagram Profile Picture Downloader

This repository contains a simple Python script that allows you to download the profile picture of an Instagram user. The script uses the `instaloader` library to achieve this.

## Project Structure

1. **.env**: This file is used to store environment variables.
2. **main.py**: The main Python script that contains the code for downloading the Instagram profile picture.
3. **requirements.txt**: A file that lists the required Python libraries. This can be generated using the `pip freeze` command.

## Getting Started

### Prerequisites

Before you begin, ensure you have met the following requirements:
- Python 3.x installed on your computer.
- pip (Python package installer) is installed.

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/wasim-shakir5/insta-dp-downloader.git
    cd insta-dp-downloader
    ```

2. Create a virtual environment (optional but recommended):
    ```sh
    python -m venv .venv
    # On linux or mac use
    source .venv/bin/activate   
    # On Windows use 
    .venv\Scripts\activate
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Finally to run the code, just type:
    ```
    python3 main.py
    ```

5. The program asks you to enter instagram username, so just type username without any symbols (@) or full url from the instagram. For example:
    ```
    wasim_shakir5 
    # Which looks like:
    (.venv) > $ python3 main.py                                                                     
    Enter Instagram username: wasim_shakir5
    ```

### .venv File

Create a `.venv` file in the root directory of your project. This file is used to store environment variables. For this simple project, you don't need any environment variables, but it's a good practice to include this step for scalability.

### main.py

The `main.py` file contains the following code:

```python
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
