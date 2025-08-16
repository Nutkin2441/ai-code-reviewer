import subprocess

def run_static_analysis(code_files):
    results = []
    for file in code_files:
        try:
            output = subprocess.check_output(['flake8', file]).decode()
            if output:
                results.append(f"{file}:\n{output}")
        except Exception as e:
            results.append(f"{file}: Error running flake8 - {e}")
    return results
