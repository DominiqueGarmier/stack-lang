### stack-lang
stack language using an infinite registry

### is it turing complete
i think so

### examples
hello world
```
python -m stack <<< "2 3 +"
```

calculate 2 ** 20
```
python -m stack <<< "0 0 STORE 1 [ 2 * 0 LOAD 1 + 0 STORE 0 LOAD 20 > LOAD APPLY ] 1 STORE 1 LOAD APPLY"
```

fill the buffer with 1's
```
python -m stack <<< "[ 1 0 LOAD APPLY ] 0 STORE 0 LOAD APPLY"
```
there is a manually set maximum numbers of instructions to avoid infinite loops
