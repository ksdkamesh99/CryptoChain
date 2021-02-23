from utils import hash
import time
timestamp = str(time.time())

class CryptoChain:
	def __init__(self):
		self.blocks=[]
		self.max_nounce=100000000
		self.pending_transactions=[]
		self.current_block=1
		transactions=[{
		'transaction_id':'f8ef5338-540e-48c3-bb5c-97be5aceaf8b',
		'timestamp':timestamp,
		'sender':'Sai Durga Kamesh Kota',
		'receiver':'ksdkamesh99',
		'amount':'100'
}]
		prevoius_hash='0000'
		self.block.append(create_block(1,transactions,prevoius_hash))

	def create_block(self,index,transactions,prevoius_hash):
		merkle_root=merkle_root(transactions)
		nounce=mining(index,transactions,prevoius_hash,merkle_root)
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
		hash_transactions=[hash(str(x)) for x in transactions]
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

