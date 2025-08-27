"""Python has functionality for interacting with JSON files
conveniently in the standard library.

JSON is python is relatively simple. You can load from files/bytes,
write to files/bytes, and use as a dict while in memory.
"""

import json
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

manifest_file = Path.cwd() / "data" / "manifest.json"


def get_data(path: Path) -> dict:
    """Reading JSON into our program.

    Usually done with json.load() or json.loads().
    Use loads to read a string or array of bytes.
    use load to read from a file on the system.
    We give load a file like object, like if we were using
    a CSV reader or another file.
    """
    with path.open() as file:
        return json.load(file)


def get_transporter_epa_ids(data: dict) -> list[str]:
    epa_ids = []
    try:
        transporters = data["transporters"]
        for transporter in transporters:
            epa_ids.append(transporter["epaId"])
    except KeyError:
        logger.warning("Error in JSON")
    return epa_ids


def main():
    data = get_data(manifest_file)
    print(get_transporter_epa_ids(data))


if __name__ == "__main__":
    main()
