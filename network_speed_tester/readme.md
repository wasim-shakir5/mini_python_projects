# Network Speed Tester

This repository contains a simple Python script that allows you to test your network speed and retrieve detailed network information. The script uses the `speedtest-cli` library to measure download and upload speeds and fetches additional network meta-information such as public IP, ISP, and location.

## Project Structure

1. **main.py**: The main Python script that contains the code for testing network speed and retrieving network information.
2. **requirements.txt**: A file that lists the required Python libraries. This can be generated using the `pip freeze` command.

## Getting Started

### Prerequisites

Before you begin, ensure you have met the following requirements:
- Python 3.x installed on your computer.
- pip (Python package installer) is installed.

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/wasim-shakir5/network-speed-tester.git
    cd network-speed-tester
    ```

2. Create a virtual environment (optional but recommended):
    ```sh
    python -m venv .venv
    # On Linux or macOS use
    source .venv/bin/activate   
    # On Windows use 
    .venv\Scripts\activate
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Finally, to run the code, just type:
    ```sh
    python main.py
    ```

5. The program will display your local and public IP addresses, ISP details, location, and the results of the speed test.

### .venv File

Create a `.venv` file in the root directory of your project. This file is used to store environment variables. For this simple project, you don't need any environment variables, but it's a good practice to include this step for scalability.

## Usage

Upon running the script, the program will automatically collect your network information and perform a speed test. It will output:

- Local IP Address
- Public IP Address
- ISP (Internet Service Provider)
- Location (City, Region, Country)
- Download Speed
- Upload Speed
- Ping (Latency)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
