import os
import sys
from argparse import ArgumentParser
from math import trunc
import json

from parse.data import *
from parse.json import parse_jeveasset_data


def cmdline_parser() -> ArgumentParser:
    parser = ArgumentParser(description='Add historical skillpoint values to JEVEAsset data for a character.')
    required = parser.add_argument_group('required arguments')

    required.add_argument("-f", "--file",
                          help="path to JEVEAsset data file", required=True)
    required.add_argument("-c", "--character",
                          help="the character name for which data is to be backfilled", required=True)
    required.add_argument("-s", "--starting-sp", type=int,
                          help="the starting amount of skillpoints for the character", metavar="N", required=True)

    return parser


if __name__ == "__main__":
    parser = cmdline_parser()
    if not len(sys.argv) > 1:
        print(parser.print_help())
        exit(1)
    args = parser.parse_args()
    parsed_data = parse_jeveasset_data(args.file)

    if args.character not in parsed_data.keys():
        print("[!] Character not found in data; exiting")
        exit(-1)

    print(f"[+] Found character {args.character} in data")

    data = parsed_data[args.character]

    last_index = find_last_zero_sp_point(data)
    sp_rate = calculate_sp_rate(data[0], data[-1], args.starting_sp)

    print(f"[D] Starting skillpoint value: {args.starting_sp:>11,}")
    print(f"[D] Final skillpoint value:    {data[-1]['skillpoints']:>11,}")
    print(f"[D] Gained over period:        "
          f"{int(skillpoint_gain(sp_rate, trunc(time_since_first_point(data[0], data[-1])))):>11,}")
    print(f"[D] {args.character} earned, on average, {trunc(sp_rate * 60000)} SP per minute from "
          f"{timestamp_to_date(data[0]['date'])} to {timestamp_to_date(data[-1]['date'])}")

    data[0]['skillpoints'] = args.starting_sp
    for index, point in enumerate(data[1:last_index+1]):
        data[index + 1]['skillpoints'] = trunc(args.starting_sp +
                                               skillpoint_gain(sp_rate, trunc(time_since_first_point(data[0], point))))

    print(f"[+] Completed interpolation of skillpoints data")

    parsed_data[args.character] = data
    new_path = os.path.join(os.path.dirname(args.file), "updated_" + os.path.basename(args.file))
    print(f"[+] Writing data to {new_path}")
    json.dump(parsed_data, open(new_path, "w"))