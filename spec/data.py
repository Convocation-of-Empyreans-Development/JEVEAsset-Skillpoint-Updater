from dataclasses import dataclass
from typing import List


@dataclass
class Asset:
    location: str
    locationid: int
    value: float


@dataclass
class Balance:
    id: int
    value: int


@dataclass
class CharacterData:
    date: int
    assets: float
    escrows: int
    escrowstocover: int
    sellorders: int
    walletbalance: int
    manufacturing: int
    contractcollateral: int
    contractvalue: int
    skillpoints: int
    balance: List[Balance]
    asset: List[Asset]


@dataclass
class JEVEAssetData:
    data: List[CharacterData]
