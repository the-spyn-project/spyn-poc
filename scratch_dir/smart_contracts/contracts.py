# GLOBAL IMPORTS
# ==================================================================================================

import json
import web3
from binascii import hexlify
from web3 import Web3, TestRPCProvider
from solc import compile_source
from web3.contract import ConciseContract
import ast

# MAIN CLASS
# ==================================================================================================

class Contract:

    def __init__(self,
                 ipc_provider,
                 contract_file_path,
                 contract_address_path,
                 contract_name,
                 contract_tx_hash):
                 
        self.ipc_provider = ipc_provider
        self.contract_file_path = contract_file_path
        self.contract_address_path = contract_address_path
        self.contract_name = contract_name
        self.contract_tx_hash = contract_tx_hash

    def load_contract(self):

        source_file = open(self.contract_file_path,'r')
        self.contract_str = source_file.read()
        source_file.close()

        self.compiled_contract = ast.literal_eval(self.contract_str)
        self.contract_interface = self.compiled_contract["<stdin>:{}".format(self.contract_name)]
        self.w3 = Web3(Web3.IPCProvider(self.ipc_provider))
        self.w3.eth.defaultAccount = self.w3.eth.accounts[0]

        tx_receipt = self.w3.eth.getTransactionReceipt(self.contract_tx_hash)
        self.contract_address = tx_receipt['contractAddress']

        self.contract_instance = self.w3.eth.contract(abi=self.contract_interface['abi'], 
                                                      address=self.contract_address)
    
    def add_device(self,port):

        tx_hash = self.contract_instance.functions.add_device(port).transact()
        print("{} was successfully added to the device list".format(port))
        print("Tx Hash: {}".format(str(hexlify(tx_hash))))

    def get_num_devices(self):

        return self.contract_instance.functions.get_all_devices().call()

    def list_all_devices(self):

        num_devices = self.get_num_devices()

        for i in range(1,num_devices):
            print('Device: {} Port: {}'
                   .format(i,self.contract_instance.functions.get_device(i).call()))


# SAMPLE CODE
# ==================================================================================================
        
if __name__ == "__main__":

    contract = Contract("/home/sadhak/Desktop/Ethereum/Blockchain/geth.ipc",
                        "/home/sadhak/Desktop/Smart_Contracts/v3/contract.txt",
                        "/home/sadhak/Desktop/Smart_Contracts/v3/tx_hash.txt",
                        "spyn",
                        b'u\x9a\xb4\xa04\x95\xc2\xda\xb1\x16\x98<\xca\xbe5\xae\x8b-.l\x19\x99\xc7\x80\xfd|\xeb^,\x0e\xf0E')

    contract.load_contract()
    contract.add_device(2324)
    print(contract.get_num_devices())
    contract.list_all_devices()


