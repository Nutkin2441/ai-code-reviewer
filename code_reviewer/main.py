import os
from code_reviewer.static_analysis import run_static_analysis
from code_reviewer.ai_api_client import run_ai_review

def scan_project(root_dir):
    code_files = []
    for subdir, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.py'):
                code_files.append(os.path.join(subdir, file))
    return code_files

def main(project_dir):
    code_files = scan_project(project_dir)
    static_results = run_static_analysis(code_files)
    ai_results = run_ai_review(code_files)
    
    # Aggregate and output results
    with open("code_review_report.md", "w") as f:
        f.write("# AI Code Review Report\n\n")
        f.write("## Static Analysis Results\n")
        for item in static_results:
            f.write(f"- {item}\n")
        f.write("\n## AI Suggestions\n")
        for item in ai_results:
            f.write(f"- {item}\n")
    print("Code review report generated: code_review_report.md")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python -m code_reviewer.main <project_dir>")
    else:
        main(sys.argv[1])
