from web3 import Web3, IPCProvider


if __name__ == "__main__":

	web3 = Web3(Web3.IPCProvider("/home/veda-sadhak/Desktop/geth/data/geth.ipc"))

	print(web3.eth.getBlock(1))

	print('------------------------------------------------------------------')

	print(web3.toWei('1','ether'))

	print('------------------------------------------------------------------')

	tx_hash = '0xf7016968aa1cbe7845d8a21a4821c5b4a867bc2336fbe24c2f5a79c6c19fa688'

	tx_data = web3.eth.getTransaction(tx_hash)

	for key , value in tx_data.items():
		print("{} -> {}".format(key,value))

	print('------------------------------------------------------------------')

	tx_receipt = web3.eth.getTransactionReceipt(tx_hash)

	for key , value in tx_receipt.items():
		print("{} -> {}".format(key,value))
	
