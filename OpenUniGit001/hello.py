import requests

# URL of the raw content on GitHub
url = "https://raw.githubusercontent.com/anuraam/OpenUniGit001/main/SourceCodeForDashboard.txt"

# Local filename to save the content
local_filename = "SourceCodeForDashboard.txt"

try:
    # Fetch the content
    response = requests.get(url)
    response.raise_for_status()  # Check for HTTP request errors

    # Save the content to a local file
    with open(local_filename, "w", encoding="utf-8") as file:
        file.write(response.text)
    
    print(f"File saved as '{local_filename}'")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
