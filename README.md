# ConCal
A simple CLI calculator written in python
<br>
## Prerequisite
Add line to `.bashrc` <br>
```bash
alias concal='python3 /path/to/file/calc.py'
```
## Usage
```bash
concal <number1> <operator> <number2>
```

This code will return:
```bash
Result: <resulting number>
```

Callback to your previous answer using the "ans" variable
```bash
concal 1 + 1
Result: 2
concal ans + 1
Result: 3
```
