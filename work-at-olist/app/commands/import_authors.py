import pandas as pd
import numpy as np
from database_create import insert_author_name
from pathlib import Path
from itertools import islice
import time
from tqdm import tqdm

start = time.time()

def batched(iterable,n=1000,strict=False):
    iterator = iter(iterable)
    while batch := tuple(islice(iterator,n)):
        if strict and len(batch) != n:
            raise ValueError
        yield batch


def import_authors_from_csv(caminho_arquivo):
    csv_reader = pd.read_csv(Path(caminho_arquivo.resolve()))
    pbar = tqdm(total=len(csv_reader))
    iter_lines = iter(csv_reader.values.tolist())

    for batch in batched (iter_lines, n=10):
        try:
            for name in batch:
                name = str(name[0]) if isinstance(name,(tuple,list,np.ndarray)) else str(name)
                pbar.update(1)
                insert_author_name(name)                
        except Exception as e:
            print(e)
    time.sleep(1)
    end = time.time()
    print(f"Total runtime of the insertion is {end-start} seconds")
    pbar.close()
if __name__ == "__main__":
    import sys
    import_authors_from_csv(Path(sys.argv[1]))