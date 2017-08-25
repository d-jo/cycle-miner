#!/usr/bin/python2

from web3 import Web3, HTTPProvider
from solc import compile_source
import json

def readABI(file):
    with open(file, 'r') as f:
        return json.load(f)

web3 = Web3(HTTPProvider('http://localhost:8545'))

abidef = readABI('testing-contract/out/TestingContract.abi')
mathContract = web3.eth.contract(abi=abidef, address='0xb4c79daB8f259C7Aee6E5b2Aa729821864227e84')

print (mathContract.call().Square(5))
