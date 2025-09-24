# TODO

## Architecture Design for Solving and Benchmarking

`main` (`Benchmark` class?)
- `@param` solver: `z3`, etc
- `@param` OOP variant: `POP`, `SSP`  
- `@param` map type: `line`, `grid`, `maze`  
- `@param` kwargs/args: problem parameters (`size`, `goal`, `budget`, `goal`, etc)



## Alternative 1:
At the root level of `dynamic_solvers` have a
- `main` script:
  - `argparser` for kwargs defining the problem instance
  - `tabler` for benchmarking and logging results
  - `benchmark` option: run the solver multiple times under memory/time tracking
- `tpMCSolver.py`: 
  - contains a Z3 solver instance
  - solves tpMC: `TPMCSolver.solve(instance: OOP)`
- `tpMCFactory.py`:
  - return OOP instance based on OOP variant and map type
- `builders` package for inheritance between problem variants:
    - `OOP` base class
    - `POP` variant package:
      - `POP` base class
      - `POPLine`
      - `POPGrid`
      - `POPMaze`
    - `SSP` variant package:
      - `SSP` base class
      - `SSPLine`
      - `SSPGrid`
      - `SSPMaze`


[//]: # (1. initialize an `OOPtpMC` `tpMC` object for the given OOP variant ad map type)
[//]: # (2. `tpMC.initProblem&#40;kwargs&#41;` loads the variables of the problem)
[//]: # (3. `tpMC.loadConstraints&#40;&#41;`)
[//]: # (4. instantiate a `TPMCSolver` `solver` object)
[//]: # (5. start benchmarking, logger?, etc)
[//]: # (6. `solver.solve&#40;&#41;`)
[//]: # (7. stop benchmarking and output results `solver.getModel&#40;&#41;`)


```
python3 -m dynamic_solvers.benchmark_runner dynamic_solvers/Pos-OOP-config.csv --output Pos-OOP-results.csv
```

## Cleanup work on API solvers & benchmarker:
 - [X] Aim for same performance/results as the file writing (match the constraints identically)
 - [X] Extend threshold parser to handle integers as well
 - [ ] 


## Versioning work
- [X] 4.15.3 - slow performance 
- [X] 4.15.1 - same issue Line249-270s SSPLine61-55s
- [X] 4.15.0 - Line249-51.5s SSPLine61-55s
- [X] 4.14.1 - Line249-51.5s SSPLine61-54s
- [X] 4.14.0 - Line249-51.7s SSPLine61-53.9s
- [X] 4.13.4 - Line249-51.4s SSPLine61-56.9s
- [X] 4.13.3 - Line249-52s SSPLine61-54.7
- [X] 4.13.2 - Line249-51.6s SSPLine61-54.6s
- [X] 4.13.1 - Line249-60s SSPLine61-60s
- [X] 4.13.0 - Line249-15.8s SSPLine61-16.5s
- [X] 4.12.4 - Line249-15.8s SSPLine61-16.5s
