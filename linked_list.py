class Node:
  def __init__(self, data) -> None:
    self.data = data
    self.head = None
    self.prev = None
  
  def __repr__(self):
    return self.data
