from flask import Flask, render_template, request, jsonify
from sonar_1 import get_sonarqube_results

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['GET'])
def analyze():
    try:
        project_key = request.form['sonarqube']
        sonarqube_url = request.form['http://localhost:9000']
        token = request.form['squ_ce97190088dd31f1371d619e356bc12120564cc6']

        # Retrieve SonarQube results
        sonar_results = get_sonarqube_results(project_key, sonarqube_url, token)

        return jsonify({'sonar_results': sonar_results})
    except KeyError as e:
        return jsonify({'error': f"Missing form field: {str(e)}"}), 400

if __name__ == '__main__':
    app.run(debug=True)
