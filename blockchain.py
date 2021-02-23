from utils import hash

class CryptoChain:
	def __init__(self):
		self.blocks=[]
		self.max_nounce=100000000
		self.pending_transactions=[]

	def create_block(self,index,transactions,nounce,prevoius_hash,merkle_root):
		string=str(index)+str(transactions)+str(nounce)+str(prevoius_hash)+str(merkle_root)
		current_hash=hash(string)
		block={}
		block['index']=index
		block['transactions']=transactions
		block['nounce']=nounce
		block['merkle_root']=merkle_root
		block['prevoius_hash']=prevoius_hash
		block['current_hash']=current_hash
		return block

	def merkle_root(self,transactions):
		hash_transactions=[hash(x) for x in transactions]
		while(len(hash_transactions)!=1):
			if len(hash_transactions)%2!=0:
				last_transaction=hash_transactions[-1]
				hash_transactions.append(hash_transactions)
			transaction_s=[]
			for i in range(0,len(hash_transactions),2):
				transaction_s.append(hash(str(hash_transactions[i])+str(hash_transactions[i+1])))
			hash_transactions=transaction_s
		merkle=hash_transactions[0]
		return merkle
	def mining(self,index,transactions,prevoius_hash,merkle_root):
		for i in range(1,self.max_nounce):
			string=str(index)+str(transactions)+str(i)+str(prevoius_hash)+str(merkle_root)
			current_hash=str(hash(string))
			if current_hash.startswith('0000'):
				return i 


		




if __name__ == '__main__':
	cc=CryptoChain()
	lister=['ssss','ssssssssss','ssssssssssssssssssssss']
	print(cc.merkle_root(lister))

