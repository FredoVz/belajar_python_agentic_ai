import shutil
from pathlib import Path

def main():
    file_name = "sample.txt"
    directory = "downloads"

    file_path = Path(f"{directory}/{file_name}")
    file_path.parent.mkdir(parents=True, exist_ok=True)

    file_path.write_text("Halo, tulisan ini disimpan ke file sample.txt")

    content = file_path.read_text(encoding="utf-8")

    print(content)

    file_path.unlink(missing_ok=True)

    shutil.rmtree(directory)

main()

# Cara debugging
# cd intermediate
# uv run 5_files_handling.py