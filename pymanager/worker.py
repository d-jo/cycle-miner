#!/usr/bin/python2

from web3 import Web3, HTTPProvider
import json

def readABI(file):
    with open(file, 'r') as f:
        return json.load(f)

def loadContract(name, address):
    a = readABI('abi/' + name)
    return web3.eth.contract(abi=a, address=address)


web3 = Web3(HTTPProvider('http://localhost:8545'))

workerContract = loadContract('TestingContract.abi', '0xee35211C4D9126D520bBfeaf3cFee5FE7B86F221')

print (workerContract.call().GetWork())
print (workerContract.call().CreateWork("this is a test asdf"))
print (workerContract.call().GetWork())
