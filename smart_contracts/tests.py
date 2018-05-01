from web3 import Web3, IPCProvider


if __name__ == "__main__":

	web3 = Web3(Web3.IPCProvider("/home/veda-sadhak/Desktop/geth/data/geth.ipc"))

	print(web3.eth.accounts)
	
