from utils import hash
class CryptoChain:
	def __init__(self):
		self.blocks=[]
		self.genesis_block=create_block(1)

	def create_block(self,index=1,transactions,nounce,prevoius_hash,merkle_root):
		string=str(index)+str(transactions)+str(nounce)+str(prevoius_hash)+str(merkle_root)
		current_hash=hash(string)
		block={}
		block['index']=index
		block['transactions']=transactions
		block['nounce']=nounce
		block['merkle_root']=merkle_root
		block['prevoius_hash']=prevoius_hash
		block['current_hash']=current_hash
	


