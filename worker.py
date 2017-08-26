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

workerContract = loadContract('TestingContract.abi', '0xb4c79daB8f259C7Aee6E5b2Aa729821864227e84')

print (workerContract.call().GetWork())
