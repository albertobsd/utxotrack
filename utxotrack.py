from colorama import Fore, Back, Style, init
import math
import sys
import os
import json
import time
import random
import requests

def dig_tx(txid,level=0):
    if(level >= max_level):
        return
    txids = []
    tx = get_tx(txid)
    if tx is None:
        print(f"There is some wrong in tx {txid}, please verify it")
        return
    if tx.get('vin') is None:
        print(f"There is some wrong in tx {txid}, please verify it")
        return
    len_vin = len(tx['vin'])
    len_vout = len(tx['vout'])
    print(f"Level {level} TX {txid} have {len_vin} inputs and {len_vout} outputs.\ninputs:")
    for vin in tx['vin']:
        txid = vin['txid']
        address = vin['prevout']['scriptpubkey_address']
        value =  vin['prevout']['value']
        
        if(txid not in txids):
            txids.append(txid)
        
        if(txid not in bittrack_dict['txids']):
            bittrack_dict['txids'].append(txid)
        else:
            print(f"Detected repeated TX id: {Fore.YELLOW}{txid}{Style.RESET_ALL}")
            
        if(address not in bittrack_dict['addresses']):
            bittrack_dict['addresses'].append(address)
        else:
            print(f"Detected repeated address: {Fore.YELLOW}{address}{Style.RESET_ALL}")
        if(txid in bittrack_dict):
            bittrack_dict[txid] +=1
        else:
            bittrack_dict[txid] = 1

        if(address in bittrack_dict):
            bittrack_dict[address] +=1
        else:
            bittrack_dict[address] = 1
    for vin in tx['vin']:
        txid = vin['txid']
        address = vin['prevout']['scriptpubkey_address']
        value =  vin['prevout']['value']
        if(bittrack_dict[txid] > 1 and bittrack_dict[address] > 1 ):
            print(f"{Fore.YELLOW}{txid}{Style.RESET_ALL} {value} from {Fore.YELLOW}{address}{Style.RESET_ALL}")
        elif(bittrack_dict[txid] > 1):
            print(f"{Fore.YELLOW}{txid}{Style.RESET_ALL} {value} from {address}")
        elif(bittrack_dict[address] > 1):
            print(f"{txid} {value} from {Fore.YELLOW}{address}{Style.RESET_ALL}")
        else:
            print(f"{txid} {value} from {address}")
    for txid in txids:
        dig_tx(txid,level+1)

def get_tx(txid):
    time.sleep(0.05)
    tx = None
    try:
        url = ""
        if networkname=="bitcoin":
            url = "https://mempool.space/api/tx/" + txid
        elif networkname=="testnet":
            url = "https://mempool.space/testnet/api/tx/" + txid
        else:
            print("Unknow network")
            exit()
        response = requests.get(url)
        if response.status_code == 200:
            tx = response.json()
            return tx
    except Exception as e:
        print(f"An error occurred: {e}")
        return tx
networknames = ['bitcoin','testnet']
networkname = ""
if len(sys.argv) == 4:
    networkname = sys.argv[1]
    target_txid = sys.argv[2]
    max_level = int(sys.argv[3])
else:
    print(f"Missing arguments expected:\npython3 {sys.argv[0]} <network> <txid> <level>")
    exit()
if(networkname not in networknames):
    print(f"Network name {networkname} unknown\nExpected names {networknames}")
    exit()
bittrack_dict = {'addresses':[],'txids':[]}
dig_tx(target_txid,0)
addresses_count = len(bittrack_dict['addresses'])
print(f"Total involved addresses: {addresses_count}")
for address in bittrack_dict['addresses']:
    if(bittrack_dict[address] > 1):
        print(f"{Fore.YELLOW}{address}{Style.RESET_ALL} : {bittrack_dict[address]}")
    else:
        print(f"{address} : {bittrack_dict[address]}")
txids_count = len(bittrack_dict['txids'])
print(f"Total involved txids: {txids_count}")
for txid in bittrack_dict['txids']:
    if(bittrack_dict[txid] > 1):
        print(f"{Fore.YELLOW}{txid}{Style.RESET_ALL} : {bittrack_dict[txid]}")
    else:
        print(f"{txid} : {bittrack_dict[txid]}")
