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
