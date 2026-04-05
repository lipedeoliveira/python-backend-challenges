import pandas as pd
import numpy as np
from app.database.database_create import insert_author_name
from pathlib import Path
from itertools import islice
import time
from tqdm import tqdm
from colorama import Fore


def import_authors_from_csv(caminho_arquivo):
    start = time.time()
    pbar = tqdm(

        total=1000000,
        desc="Inserting Batch's'",
        bar_format='[{desc}: {elapsed}<{remaining}] {n_fmt}/{total_fmt} | {l_bar}{bar} {rate_fmt}{postfix}',
        colour='green'
    )

    try:
        for chunk in pd.read_csv(caminho_arquivo,chunksize=1000):
            insert_author_name(chunk.values)
            pbar.update(len(chunk))
    except Exception as e:
        pbar.write(Fore.RED+str(e))
    end = time.time()
    
    print(f"Total runtime of the insertion is {end-start} seconds")
    pbar.close()

if __name__ == "__main__":
    import sys
    import_authors_from_csv(Path(sys.argv[1]))