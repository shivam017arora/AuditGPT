import streamlit as st
import requests
import os
import tempfile


def save_code_file(file):
    _, temp_file_path = tempfile.mkstemp(suffix=".sol")  # Create a temporary file with .sol extension
    with open(temp_file_path, "wb") as f:
        f.write(file.getvalue())
    return temp_file_path

def read_code_file(file_path):
    with open(file_path, "r") as f:
        code = f.read()
    return code


def send_post_request(code_file_path, language):
    url = "http://127.0.0.1:5002"  # Replace with your actual endpoint URL
    files = {"code_file": open(code_file_path, "rb")}
    data = {"language": language}

    try:
        response = requests.post(url, files=files, data=data)
        response.raise_for_status()
        return response.json(), response.status_code
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}, 500

def main():
    st.title("Code File Viewer")
    # Language selection
    language = "solidity"
    
    code_file = st.file_uploader("Upload a code file", type=["py", "java", "cpp", "sol"])

    if code_file is not None:
        # Save file
        code_file_path = save_code_file(code_file)

        # Display file contents
        code = read_code_file(code_file_path)
        st.code(code, line_numbers=True)

        # Make POST request
        if st.button("Audit"):
            response, status_code = send_post_request(code_file_path, language)

            st.json(response)

            # Display status code
            st.write("Status code:", status_code)

        # Remove temporary file
        os.remove(code_file_path)


if __name__ == "__main__":
    main()
