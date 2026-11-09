# _generator/build.py
import os
import sys

# Add _generator directory to sys.path
generator_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, generator_dir)

from layout import build_full_html

def main():
    print("Building SWD392 Master Study Guide index.html...")
    html_content = build_full_html()
    
    out_path = os.path.join(os.path.dirname(generator_dir), "index.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    
    file_size_kb = os.path.getsize(out_path) / 1024
    print(f"Successfully generated index.html at: {out_path}")
    print(f"File size: {file_size_kb:.2f} KB ({len(html_content.splitlines())} lines)")

if __name__ == "__main__":
    main()

