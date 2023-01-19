from typing import Callable, Sequence, Any
from math import ceil
from multiprocessing import cpu_count, Pool

def get_n_jobs(n_jobs: int = -1) -> int:
    if n_jobs < 0:
        n_jobs = cpu_count()
    elif n_jobs == 0:
        n_jobs == 1
    elif n_jobs > cpu_count():
        n_jobs = cpu_count()

    return n_jobs

def mp(
    func: Callable[[Any], Any],
    seq: Sequence[Any],
    n_jobs: int = -1,
    chunk_size: int  = None,
) -> list:

    n_jobs = get_n_jobs(n_jobs)

    if chunk_size is None:
        chunk_size = ceil(len(seq) / n_jobs)

    if n_jobs == 1:
        return [func(item) for item in seq]
    else:
        with Pool(n_jobs) as pool:
            return pool.map(func, seq, chunksize=chunk_size)