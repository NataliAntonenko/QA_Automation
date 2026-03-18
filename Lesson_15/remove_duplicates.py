import csv
from pathlib import Path


base_dir = Path(__file__).parent
csv_dir = base_dir / "work_with_csv"

file1 = csv_dir / "random.csv"
file2 = csv_dir / "random-michaels.csv"

result_file = base_dir / "result_antonenko.csv"


unique_rows = set()

for file_path in [file1, file2]:
    with file_path.open("r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            unique_rows.add(tuple(row))


with result_file.open("w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    for row in unique_rows:
        writer.writerow(row)