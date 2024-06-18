import subprocess

def run_sonarqube_analysis():
    """ Run SonarQube analysis using the sonar-scanner CLI. """
    subprocess.run(['C:/Users/praka/Downloads/Software/solar-scanner/bin/sonar-scanner'], check=True)

# Example usage
run_sonarqube_analysis()