import unittest
from Deque_Generator import get_deque, LL_DEQUE_TYPE, ARR_DEQUE_TYPE
from Stack import Stack
from Queue import Queue

class DSQTester(unittest.TestCase):
   
   def setUp(self):
      # Run your tests with each deque type to ensure that
      # they behave identically.
      self.__deque = get_deque(LL_DEQUE_TYPE)
      self.__stack = Stack()
      self.__queue = Queue()

#Testing for an empty stack

   def test_stack_empty_list_string(self):
      self.assertEqual('[ ]', str(self.__stack), 'An empty list will print "[ ]"')
      
   def test_stack_len_empty(self):
      out = len(self.__stack)
      self.assertEqual(0, out)
      
   def test_stack_peek_empty(self):
      out = self.__stack.peek()
      self.assertEqual(None, out)
      
   def test_stack_pop_empty(self):
      out = self.__stack.pop()
      self.assertEqual(None, out)
      
#Testing for a stack of 1

   def test_stack_push_one(self):
      self.__stack.push('Data')
      self.assertEqual('[ Data ]', str(self.__stack))
   
   def test_stack_push_one_length(self):
      self.__stack.push('Data')
      out = len(self.__stack)
      self.assertEqual(1, out)
      
   def test_stack_peek_one(self):
      self.__stack.push('Rocks')
      out = self.__stack.peek()
      self.assertEqual('Rocks', out)
      
   def test_stack_pop_one(self):
      self.__stack.push('Structures')
      out = self.__stack.pop()
      self.assertEqual('Structures', out)
      
   def test_stack_pop_one_empty(self):
      self.__stack.push('Structures')
      self.__stack.pop()
      length = len(self.__stack)
      self.assertEqual(0, length)
      
#Testing for a stack of 2

   def test_stack_len_two_push(self):
      self.__stack.push('Data')
      self.__stack.push('Victory')
      out = len(self.__stack)
      self.assertEqual(2, out)
      
   def test_stack_string_two_push(self):
      self.__stack.push('Data')
      self.__stack.push('Victory')
      self.assertEqual('[ Victory, Data ]', str(self.__stack))
      
   def test_stack_two_peek_element(self):
      self.__stack.push('Data')
      self.__stack.push('Money')
      out = self.__stack.peek()
      self.assertEqual('Money', out)
      
   def test_stack_two_pop_element(self):
      self.__stack.push('Data')
      self.__stack.push('Money')
      out = self.__stack.pop()
      self.assertEqual('Money', out)
      
#Testing for a stack of 3

   def test_stack_len_three_push(self):
      self.__stack.push('Data')
      self.__stack.push('Victory')
      self.__stack.push(9)
      out = len(self.__stack)
      self.assertEqual(3, out)
      
   def test_stack_string_three_push(self):
      self.__stack.push('Data')
      self.__stack.push('Victory')
      self.__stack.push('Computers')
      self.assertEqual('[ Computers, Victory, Data ]', str(self.__stack))
      
   def test_stack_three_peek_element(self):
      self.__stack.push('Data')
      self.__stack.push('Money')
      self.__stack.push('Victory')
      out = self.__stack.peek()
      self.assertEqual('Victory', out)
      
   def test_stack_three_pop_element(self):
      self.__stack.push('Stack')
      self.__stack.push('Money')
      self.__stack.push('Victory')
      out = self.__stack.pop()
      self.assertEqual('Victory', out)
      
#Testing for an empty queue

   def test_queue_empty_list_string(self):
      self.assertEqual('[ ]', str(self.__queue), 'Empty list should print as "[ ]"')
      
   def test_queue__len_empty_q(self):
      out = len(self.__queue)
      self.assertEqual(0, out)
      
   def test_queue_pop_empty(self):
      out = self.__queue.dequeue()
      self.assertEqual(None, out)
      
#Testing for 1 queue
 
   def test_queue_one_string(self):
      self.__queue.enqueue('Data')
      self.assertEqual('[ Data ]', str(self.__queue))
      
   def test_queue_len_one(self):
      self.__queue.enqueue('Data')
      out = len(self.__queue)
      self.assertEqual(1, out)
      
   def test_queue_pop_one(self):
      self.__queue.enqueue('Data')
      out = self.__queue.dequeue()
      self.assertEqual('Data', out)
      
#Testing for 2 queue

   def test_queue_two_string(self):
      self.__queue.enqueue('Data')
      self.__queue.enqueue('Money')
      self.assertEqual('[ Data, Money ]', str(self.__queue))
      
   def test_queue_len_two(self):
      self.__queue.enqueue('Data')
      self.__queue.enqueue('Money')
      out = len(self.__queue)
      self.assertEqual(2, out)
      
   def test_queue_pop_two(self):
      self.__queue.enqueue('Data')
      self.__queue.enqueue('Money')
      out = self.__queue.dequeue()
      self.assertEqual('Data', out)
      
#Testing for 3 queue

   def test_queue_three_string(self):
      self.__queue.enqueue('Data')
      self.__queue.enqueue('Money')
      self.__queue.enqueue('Victory')
      self.assertEqual('[ Data, Money, Victory ]', str(self.__queue))
      
   def test_queue_len_three(self):
      self.__queue.enqueue('Data')
      self.__queue.enqueue('Money')
      self.__queue.enqueue('Victory')
      out = len(self.__queue)
      
   def test_queue_pop_three(self):
      self.__queue.enqueue('Data')
      self.__queue.enqueue('Money')
      self.__queue.enqueue('Victory')
      out = self.__queue.dequeue()
      self.assertEqual('Data', out)
      
#Testing for an empty deque

   def test_deque_empty_list_insert(self):
      self.assertEqual('[ ]', str(self.__deque), 'Empty list should print as "[ ]"')
   
   def test_deque_len_empty(self):
      out = len(self.__deque)
      self.assertEqual(0, out)

   def test_deque_peek_front_empty(self):
      out = self.__deque.peek_front()
      self.assertEqual(None, out)
      
   def test_deque_peek_back_empty(self):
      out = self.__deque.peek_back()
      self.assertEqual(None, out)
      
   def test_deque_pop_front_empty_list(self):
      out = self.__deque.pop_front()
      self.assertEqual(None, out)
      
   def test_deque_pop_back_empty_list(self):
      out = self.__deque.pop_back()
      self.assertEqual(None, out)
      
#Testing for 1 deque
      
   def test_deque_push_front_one(self):
      self.__deque.push_front('Data')
      self.assertEqual('[ Data ]', str(self.__deque))
      
   def test_deque_push_front_one_length(self):
      self.__deque.push_front('Data')
      out = len(self.__deque)
      self.assertEqual(1, out)
      
   def test_deque_peek_front_one(self):
      self.__deque.push_front('Rocks')
      out = self.__deque.peek_front()
      self.assertEqual('Rocks', out)
      
   def test_deque_pop_front_one(self):
      self.__deque.push_front('Structures')
      out = self.__deque.pop_front()
      self.assertEqual('Structures', out)
      
   def test_deque_pop_front_one_empty(self):
      self.__deque.push_front('Structures')
      self.__deque.pop_front()
      length = len(self.__deque)
      self.assertEqual(0, length)
      
   def test_deque_push_back_one(self):
      self.__deque.push_back('Data')
      self.assertEqual('[ Data ]', str(self.__deque))
      
   def test_deque_peek_back_one(self):
      self.__deque.push_back('Mouse')
      out = self.__deque.peek_back()
      self.assertEqual('Mouse', out)
      
   def test_deque_pop_back_one(self):
      self.__deque.push_back('Keyboard')
      out = self.__deque.pop_back()
      self.assertEqual('Keyboard', out)
      
   def test_deque_pop_back_one_empty(self):
      self.__deque.push_back('Structures')
      self.__deque.pop_back()
      length = len(self.__deque)
      self.assertEqual(0, length)
      
#Testing for 2 deque

   def test_deque_len_two_push_front(self):
      self.__deque.push_front('Data')
      self.__deque.push_front('Victory')
      out = len(self.__deque)
      self.assertEqual(2, out)
      
   def test_deque_string_two_push_front(self):
      self.__deque.push_front('Data')
      self.__deque.push_front('Victory')
      self.assertEqual('[ Victory, Data ]', str(self.__deque))
      
   def test_deque_string_two_back_front(self):
      self.__deque.push_back('Victory')
      self.__deque.push_back(9)
      self.assertEqual('[ Victory, 9 ]', str(self.__deque))
      
   def test_deque_two_peek_element_front(self):
      self.__deque.push_front('Data')
      self.__deque.push_front('Money')
      out = self.__deque.peek_front()
      self.assertEqual('Money', out)
      
   def test_deque_two_peek_back(self):
      self.__deque.push_front('Data')
      self.__deque.push_front('Money')
      out = self.__deque.peek_back()
      self.assertEqual('Data', out)
      
   def test_deque_two_pop_element_front(self):
      self.__deque.push_front('Data')
      self.__deque.push_front('Money')
      out = self.__deque.pop_front()
      self.assertEqual('Money', out)
      
   def test_deque_two_pop_element_back(self):
      self.__deque.push_front('Data')
      self.__deque.push_front('Money')
      out = self.__deque.pop_back()
      self.assertEqual('Data', out)
      
#Testing for 3 deque

   def test_deque_string_three_front(self):
      self.__deque.push_front('Victory')
      self.__deque.push_front(9)
      self.__deque.push_front('Data')
      self.assertEqual('[ Data, 9, Victory ]', str(self.__deque))
      
   def test_deque_string_three_back(self):
      self.__deque.push_back('Victory')
      self.__deque.push_back(9)
      self.__deque.push_back('Data')
      self.assertEqual('[ Victory, 9, Data ]', str(self.__deque))
      
   def test_deque_three_len_back(self):
      self.__deque.push_back('Victory')
      self.__deque.push_back(9)
      self.__deque.push_back('Data')
      out = len(self.__deque)
      self.assertEqual(3, out)
      
   def test_deque_three_pop_front(self):
      self.__deque.push_front('Victory')
      self.__deque.push_front(9)
      self.__deque.push_front('Data')
      out = self.__deque.pop_front()
      self.assertEqual('Data', out)
      
   def test_deque_three_pop_back(self):
      self.__deque.push_back('Victory')
      self.__deque.push_back(9)
      self.__deque.push_back('Data')
      out = self.__deque.pop_back()
      self.assertEqual('Data', out)
      
   def test_deque_three_pop_len_front(self):
      self.__deque.push_back('Victory')
      self.__deque.push_back(9)
      self.__deque.push_back('Data')
      self.__deque.pop_front()
      out = len(self.__deque)
      self.assertEqual(2, out)
      
   def test_deque_three_pop_len_back(self):
      self.__deque.push_back('Victory')
      self.__deque.push_back(9)
      self.__deque.push_back('Data')
      self.__deque.pop_back()
      out = len(self.__deque)
      self.assertEqual(2, out)
      
   def test_deque_three_peek_front(self):
      self.__deque.push_front('Victory')
      self.__deque.push_front(9)
      self.__deque.push_front('Data')
      out = self.__deque.peek_front()
      self.assertEqual('Data', out)
      
   def test_deque_three_peek_back(self):
      self.__deque.push_back('Victory')
      self.__deque.push_back(9)
      self.__deque.push_back('Data')
      out = self.__deque.peek_back()
      self.assertEqual('Data', out)

       
  # TODO add your test methods here. Like Linked_List_Test.py,
  # each test should me in a method whose name begins with test_

if __name__ == '__main__':
   unittest.main()