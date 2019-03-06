from Deque_Generator import get_deque

class Stack:

   def __init__(self):
      self._dequ = get_deque()
     
   def __str__(self):
      # TODO replace pass with your implementation.
      #pass
      return str(self._dequ)
   
   def __len__(self):
      # TODO replace pass with your implementation.
      #pass
      return len(self._dequ)
     
   def push(self, val):
      # TODO replace pass with your implementation.
      #pass
      self._dequ.push_front(val)

   def pop(self):
      # TODO replace pass with your implementation.
      #pass
      return self._dequ.pop_front()

   def peek(self):
      # TODO replace pass with your implementation.
      #pass
      return self._dequ.peek_front()

# Unit tests make the main section unneccessary.
#if __name__ == '__main__':
#  pass
