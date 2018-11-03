class Block():  # create Block class

# Set constructor to initialize new block instances
	def __init__(index, timestamp, data, previousHash=''):
		# TODO : add datatype to args comment
		""" Constructor, the class initializer method.
		Args:
      index (): shows where the block exists on the chain
      timestamp (): timestamp stores when the block was created
      data (): data stored in the block
      previousHash (): Stores the hash of the preceeding block before

    """
		self.index = index
		self.timestamp = timestamp
		self.data = data
		self.previousHash = previousHash
		self.hash = ''  # block hash



