import requests
from requests.auth import HTTPBasicAuth

def get_sonarqube_results(project_key, sonarqube_url, token):
    """ Retrieve analysis results from SonarQube. """
    url = f"{sonarqube_url}/api/issues/search?projectKeys={project_key}"
    
    # Split the token into username and password parts
    username = token
    password = ''  # No password is used, only the token
    
    try:
        response = requests.get(url, auth=HTTPBasicAuth(username, password))
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"HTTP Request failed: {e}")
        if response:
            print(f"Response status code: {response.status_code}")
            print(f"Response content: {response.text}")
        return None

# Example usage
sonarqube_url = 'http://localhost:9000'
project_key = 'sonarqube'
token = 'squ_ce97190088dd31f1371d619e356bc12120564cc6'  # Replace with your actual token

results = get_sonarqube_results(project_key, sonarqube_url, token)
if results:
    print(results)
else:
    print("Failed to retrieve SonarQube results.")
