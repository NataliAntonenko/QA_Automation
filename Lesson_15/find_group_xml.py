import logging
from pathlib import Path
import xml.etree.ElementTree as ET


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def get_incoming_by_group_number(group_number: str):
    base_dir = Path(__file__).parent
    xml_path = base_dir / "work_with_xml" / "groups.xml"

    tree = ET.parse(xml_path)
    root = tree.getroot()

    for group in root.findall("group"):
        number = group.find("number")

        if number is not None and number.text == group_number:
            incoming = group.find("timingExbytes/incoming")

            if incoming is not None:
                return incoming.text

    return None


result = get_incoming_by_group_number("1")

logging.info(f"incoming value for group 1: {result}")