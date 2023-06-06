import openai

def read_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    return lines

def format_bug_file(lines, language):
    formatted_lines = []
    formatted_lines.append("##### Fix bugs in the below function\n")
    formatted_lines.append(f"\n### Buggy {language}\n")
    for i, line in enumerate(lines, start=1):
        formatted_lines.append(f"LINE{i}, {line}")
    formatted_string = ''.join(formatted_lines)
    return formatted_string


def run_api(data):
    res = openai.Completion.create(
        model="text-davinci-003",
        prompt=data,
        temperature=0,
        max_tokens=3000,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["###"],
    )
    print(res.choices[0].text)
    return res.choices[0].text