# Pinger

`pinger` is a Python3 project created to ping websites using multithreading.

## Run

```
python pingermain.py
```

```
usage: pingermain.py [-h] [--pool POOL] [--iterations ITERATIONS]

Ping some websites.

optional arguments:
-h, --help            show this help message and exit
  --parallel PARALLEL   Number of jobs to run in parallel
  --iterations ITERATIONS
                        Number of times to ping each website
  --processor {process,thread}
                        Parallel processor implementation.

```

### Defaults
Default `pool` set to 5 <br>
Default `iterations` set to 5
Default `processor` set to `thread`

## Data

`pinger` will ping websites in the `hosts` array in `data.json`

