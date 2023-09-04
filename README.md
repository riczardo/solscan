# solscan - smart contracts vulnerability scanner

<img src="/logo.png" width="300"/>
Solscan is a static Solidity vulnerabilities scanner written in Python. It works based on regular expressions and contextual analyse of your code. Solscan is able to scan contracts regargless of their version or ability to compile (you can even scan a single function without a need to have a whole smart contract ready).


## Features
* Support of 28 vulnerabilities
* Static scan of your code meaning no need to have compiler
* Works on all Solidity versions

## Installation
### Prerequisites
First of all, you will need to have Python 3.7+ installed on your machine.
Tool also uses `click`, `termcolor` and `pyfiglet` python packages.

### How to install the tool?

First, clone the repository into your local machine:
```
git clone https://github.com/riczardo/solscan
```

Next, you will need click python library. You can download it by:
```
pip install click
```
If you encounter any problem with the library, you can try to install it into folder containg the tool.

```
pip install --target=/path/to/the/tool click
```
Same goes to the rest of the libraries. Install termcolor and pyfiglet library:
```
pip install termcolor
```
```
pip install pyfiglet
```
After that you should be good to go.

## Usage
To use the tool, go to the solscan directory, then use following command:
```
python3 main.py scan /path/to/your/contract.sol
```
After the scan is completed, you will get the results and corresponding recommendations.
## Detectors

Solscan gives you the ability to scan your smart contract code to find some underlying vulnerabilities listed below:
| ID | VULNERABILITY                |
|----|------------------------------|
| 1  | ArbitraryFrom                |
| 2  | Assembly                     |
| 3  | Assert Violation             |
| 4  | Bad Assignment Operator      |
| 5  | Delegate Call                |
| 6  | Blockhash                    |
| 7  | Callcode                     |
| 8  | Msgas                        |
| 9  | Now                          |
| 10 | Sha3                         |
| 11 | Throw                        |
| 12 | Dynamic Array Length         |
| 13 | Ether Lock                   |
| 14 | Floating Pragma              |
| 15 | Functions Default Visibility |
| 16 | Hash Colission               |
| 17 | Insecure Randomsource        |
| 18 | Int Over/underflow           |
| 19 | Looped Calls                 |
| 20 | Multidigits                  |
| 21 | Reentrancy                   |
| 22 | RTLO                         |
| 23 | Selfdestruct                 |
| 24 | Stored credentials           |
| 25 | Strict Equality              |
| 26 | TX-Origin                    |
| 27 | Unchecked external call      |
| 28 | Wrong Constructor Name       |
