import os

def collect_code_files(directory):
    print(directory)
    """ Collect code files from a specified directory. """
    code_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(('.py', '.js', '.java', '.cpp')):  # Add more extensions as needed
                code_files.append(os.path.join(root, file))
    return code_files

# Example usage
code_files = collect_code_files('.')
print(code_files)
