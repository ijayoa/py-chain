import hashlib  # python module for hashinn funtions including SHA256
from json import dumps # need this to covert JSON data to string


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
    self.hash = this.createBlockHash()  # generated hash for the block


  def createBlockHash():
    # TODO : fix overflowing code
    """Given a block's property calculate return Hash from Hash function"""
    compute_data = this.index + this.previousHash + this.timestamp + dumps(this.data)
    return hashlib.sha256(b"{}".format(compute_data)).hexdigest()
