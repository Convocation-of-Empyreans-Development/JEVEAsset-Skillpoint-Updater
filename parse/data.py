import datetime
from typing import List

from spec.data import CharacterData, JEVEAssetData


def get_date_range(data: List[CharacterData]) -> float:
    """
    Get the number of milliseconds between the first and last data point in the set.
    :param data: the dataset for a character from JEVEAsset
    :return: the time in seconds between start and end of provided data
    """
    timestamps = [point["date"] for point in data]
    return max(timestamps) - min(timestamps)


def time_since_first_point(first: CharacterData, current: CharacterData) -> float:
    """
    Calculate the number of milliseconds between two data points.
    :param first: the first datapoint
    :param current: the given datapoint
    :return: the time in seconds between two data points
    """
    return current["date"] - first["date"]


def calculate_sp_rate(first: CharacterData, last: CharacterData, starting_skillpoints: int) -> float:
    """
    Calculate the average rate of skillpoint gain over the period between two data points.
    :param first: the first data point
    :param last: the last data point
    :param starting_skillpoints: the given starting value for the first data point
    :return: the average skillpoint gain rate (points per second)
    """
    return (last["skillpoints"] - starting_skillpoints) / time_since_first_point(first, last)


def find_last_zero_sp_point(data: JEVEAssetData) -> int:
    """
    Find the index of the last data point to contain a zero value for the skillpoint attribute.
    :param data: The character's JEVEAsset data
    :return: the index of the data point
    """
    for index, point in enumerate(data):
        if point["skillpoints"] != 0:
            return index


def timestamp_to_date(timestamp: int) -> str:
    """
    Convert UNIX timestamp in milliseconds to date.
    :param timestamp:
    :return: the date converted from the timestamp
    """
    return datetime.datetime.fromtimestamp(timestamp / 1000).strftime("%Y-%m-%d %H:%M:%S")


def skillpoint_gain(rate: float, delta: int) -> float:
    """
    Calculate the amount of skillpoints gained in a given period of time
    :param rate: the rate of skillpoint gain in points per millisecond
    :param delta: the amount of milliseconds measured
    :return: the amount of skillpoints gained
    """
    return rate * delta
