import os
import json
from flask import Flask, request, jsonify
from flask_cors import CORS
from vulnerable.helper import format_bug_file, read_file, run_api
from dotenv import load_dotenv
load_dotenv('.env')

app = Flask(__name__)
CORS(app=app)


@app.route('/', methods=['POST'])
def main():
    code_file = request.files.get('code_file')
    language = request.form.get('language')

    if code_file is not None and language is not None:
        filename = 'bug.sol'
        code_file.save(filename)
        
        lines = read_file(filename)
        formatted_code = format_bug_file(lines, language)

        data = f""" 
        {formatted_code}
            
        FORMAT of response:
        {
        "Line: <int>,"
        "Reason: <string>,"
        "HowToFix: <string>"
        }
            ### JSON:
            """
        try:
            res = run_api(data)
            os.remove(filename)
            response_json = json.loads(res)

            return jsonify(response_json), 200
        except Exception as e:
            # Handle the exception and return an error response
            error_message = str(e)
            return jsonify({'error': error_message}), 500
    else:
        return 'Invalid request.'

if __name__ == "__main__":
    app.run(debug=True, port=5002, host='0.0.0.0')