import re
import sys


# Print usage if there is too many or no arguments provided
if len(sys.argv) < 2:
    print("Usage: python script_name.py <file_path>")
    sys.exit(1)
elif len(sys.argv) > 2:
    print("Usage: python script_name.py <file_path>")
    sys.exit(1)

# Set file_path to be argument when running the script.
file_path = sys.argv[1]


def extract_ips_from_report(file_path):
    ip_pattern = r'ReportHost name="([0-9]{1,3}(?:\.[0-9]{1,3}){3})"' # Regular expression to match the IP address in the ReportHost tag
    with open(file_path, 'r') as file: # Open and read the file content
        content = file.read()  # Read the entire file content
    ips = re.findall(ip_pattern, content) # Find all matches and store them in a list
    return ips  # Return the list of IPs


def extract_package_sections_from_file(file_path):
    pattern = r"Here is the list of packages installed on the remote Red Hat Linux system :\s*(.*?)\s*</plugin_output>" # Regular expression to capture text between the two markers
    with open(file_path, 'r') as file: # Open and read the file content
        data = file.read()
    
    matches = re.findall(pattern, data, re.DOTALL)  # Find all matches and return as a list
    return matches



ip_list = extract_ips_from_report(file_path) # Extract ips


package_sections = extract_package_sections_from_file(file_path) # Extract package sections


for ip, section in zip(ip_list, package_sections): # Iterate over both IPs and package sections
    print(f"IP: {ip}")
    lines = section.splitlines() # Split the section into lines
   
    firefox_lines = [line for line in lines if re.search(r'firefox', line, re.IGNORECASE)]  # Filter and display only the first line containing 'firefox' (case-insensitive)
    python_lines = [line for line in lines if re.search(r'python3-bind', line, re.IGNORECASE)]
    bind_lines = [line for line in lines if re.search(r'bind', line, re.IGNORECASE)]
    
    if firefox_lines or python_lines:  # If there are any lines with 'firefox'
        print(f"{firefox_lines[0].strip()}")  # Print the first matching line
        print(f"{python_lines[0].strip()}")  # Print the first matching line
        print(f"{bind_lines[0].strip()}")
    print("-" * 40)