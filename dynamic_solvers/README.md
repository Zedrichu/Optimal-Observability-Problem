# Scaling Observation-aware Planning in Uncertain Domains

# Docker

One can use docker to run all scripts. The corresponding Dockerfile is part of this repository.
To build it, run the following commands **from the root directory** of the repository:

```
docker build -f dynamic_solvers/Dockerfile -t artifact .
```
After that, the following command opens a shell in which one can run the scripts:

```
docker run -it artifact /bin/bash
```

For example, the following two commands can then be used to reproduce table 1 and table 2 from the paper:

```
python3 -m dynamic_solvers.benchmark dynamic_solvers/PD-OOP-config.csv --output dynamic_solvers/PD-OOP-results.csv

python3 -m dynamic_solvers.benchmark dynamic_solvers/Pos-OOP-config.csv --output dynamic_solvers/Pos-OOP-results.csv

```

Batch edit timeout setting for benchmarking (default = 90000ms):
```
sed -i 's/<CURRENT_TIMEOUT>/<NEW_TIMEOUT_MS>/g' <CONFIG-FILE>
```