#!/usr/bin/evn python3

import csv
import bz2
import requests
import io
import pickle

CHUNK_SIZE = 1024


def download():
    r = requests.get('https://www.fuzzwork.co.uk/dump/latest/invTypes.csv.bz2', stream=True)

    kv = {}

    with io.BytesIO() as dIO:
        decompressor = bz2.BZ2Decompressor()

        for chunk in r.iter_content(CHUNK_SIZE):
            dIO.write(decompressor.decompress(chunk))

        dIO.seek(0)

        with io.TextIOWrapper(dIO, encoding='utf8') as t:
            c = csv.DictReader(t)
            for row in c:
                kv[row['typeName']] = row['typeID']

    return kv


if __name__ == "__main__":
    with open('invTypes.pyobj', 'wb') as f:
        pickle.dump(download(), f)
