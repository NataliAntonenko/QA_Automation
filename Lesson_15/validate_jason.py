import json
import logging
from pathlib import Path

logging.basicConfig(
    filename="json__antonenko.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

folder_path = Path(__file__).parent

for file_path in folder_path.glob("*.json"):
    try:
        with file_path.open("r", encoding="utf-8") as f:
            json.load(f)

    except json.JSONDecodeError as e:
        logging.error(f"Invalid JSON file: {file_path.name} | Error: {e}")