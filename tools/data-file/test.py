# -*- coding: utf-8 -*-

import random
import polars as pl
from faker import Faker

fake = Faker()


def random_float() -> float:
    return random.randint(1, 10000) / 100.0


n = 1000
df = pl.DataFrame({
    "category": [fake.word() for _ in range(n)],
    "sub_category": [fake.word() for _ in range(n)],
    "name": [fake.word() for _ in range(n)],
    "x": [random_float() for _ in range(n)],
    "y": [random_float() for _ in range(n)],
    "z": [random_float() for _ in range(n)],
})
df.write_csv("test.csv")
df.write_json("test.json")
df.write_parquet("test.parquet")
df.write_ipc("test.feather", compression="lz4")

