import json
from typing import Dict

from spec.data import JEVEAssetData


def parse_jeveasset_data(path: str) -> Dict[str, JEVEAssetData]:
    """
    Parse the given JEVEAsset data file.
    The file is structured as JSON, with each EVE character given as a key.

    :param path: the path to the file containing JEVEAsset data
    :return: a dictionary mapping characters to their respective data.
    """
    try:
        with open(path) as data:
            data = json.load(open(path))
    except IOError:
        print("Could not find the specified file; exiting")
        exit(-1)
    else:
        characters = dict()
        for character_name, character_data in data.items():
            characters[character_name] = JEVEAssetData(data)

    print(f"[+] Found {len(data.keys())} characters in {path}")
    return data
