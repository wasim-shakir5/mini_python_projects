import speedtest  # Import the speedtest library to measure internet speed
import socket  # Import the socket library to retrieve IP address
import requests  # Import requests to make HTTP requests to retrieve public IP info
import platform  # Import platform to get system information

def get_network_info():
    # Get the local IP address of the machine
    local_ip = socket.gethostbyname(socket.gethostname())

    # Get public IP and ISP details using ipinfo.io API
    try:
        response = requests.get('https://ipinfo.io')  # Make a request to the IP info API
        data = response.json()  # Parse the JSON response
        public_ip = data.get('ip') 
        isp = data.get('org') 
        city = data.get('city') 
        region = data.get('region') 
        country = data.get('country') 
    except requests.ConnectionError:
        # If there's a connection error, set values to indicate failure
        public_ip = "Unable to retrieve public IP"
        isp = "Unable to retrieve ISP"
        city = region = country = "N/A"

    return {
        'local_ip': local_ip,
        'public_ip': public_ip,
        'isp': isp, 
        'city': city, 
        'region': region, 
        'country': country  
    }

def test_speed():
    # Create an instance of the Speedtest class
    st = speedtest.Speedtest()

    # Find the best server based on ping
    st.get_best_server()

    # Measure download speed and convert to Mbps
    download_speed = st.download() / 1_000_000  # Convert from bits to Megabits

    # Measure upload speed and convert to Mbps
    upload_speed = st.upload() / 1_000_000  # Convert from bits to Megabits

    # Measure ping (latency) in milliseconds
    ping_result = st.results.ping

    # Return a dictionary containing speed test results
    return {
        'download_speed': download_speed, 
        'upload_speed': upload_speed, 
        'ping': ping_result  
    }

def get_system_info():
    # Gather system information using the platform library
    system_info = {
        "platform": platform.system(),  # Get the operating system name
        "platform_version": platform.version(),  # Get the OS version
        "architecture": platform.machine(),  # Get the machine architecture (e.g., x86_64)
        "hostname": socket.gethostname()  # Get the hostname of the machine
    }
    return system_info  # Return the system information dictionary

if __name__ == '__main__':
    print("Collecting network information...")
    network_info = get_network_info() 

    # Print the retrieved network information
    print(f"Local IP: {network_info['local_ip']}")
    print(f"Public IP: {network_info['public_ip']}")
    print(f"ISP: {network_info['isp']}")
    print(f"Location: {network_info['city']}, {network_info['region']}, {network_info['country']}\n")

    print("Running speed test...")
    speed_info = test_speed()  

    print(f"Download Speed: {speed_info['download_speed']:.2f} Mbps")
    print(f"Upload Speed: {speed_info['upload_speed']:.2f} Mbps")
    print(f"Ping: {speed_info['ping']} ms\n")

    print("System Information:")
    system_info = get_system_info() 

    for key, value in system_info.items():
        print(f"{key.capitalize()}: {value}") 
