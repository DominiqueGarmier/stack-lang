1 1 STORE # counter
1 2 STORE # last fib
0 3 STORE # 2nd last fib
15 4 STORE # N

[ 2 LOAD 3 LOAD + ] -1 STORE # compute new fib
[ -1 LOAD APPLY 2 LOAD 3 STORE 2 STORE ] -2 STORE # load compute and store fib
[ -2 LOAD APPLY 1 LOAD 1 + DUP 1 STORE 4 LOAD > -3 * LOAD APPLY ] -3 STORE # run the above line in a loop 10 times

[ 2 LOAD ] 0 STORE

-3 LOAD APPLY
