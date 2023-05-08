# DL Practices

This is a submission for the "Big Numbers" practice. 


## Project structure

**src/big_numbers.py** contains the implementation of the class BigNumber.

**src/U64.py** contains the implementation of the class U64, which emulates unsigned integer of 64 bits with overflows 
and so on. It is used by the BigNumber class.

**tests/** folder contains the unit tests.

## Setup

First of all, create a virtual environment and install the requirements:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```


## Usage

To run the unit tests, execute the following command:

```bash
pytest
```
or 
```bash
python -m pytest
```
