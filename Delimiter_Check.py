import sys # for sys.argv, the command-line arguments
from Stack import Stack

def delimiter_Test(filename):
  stack = Stack()
  stack.push("x")
  data = open(filename, 'r')
  for row in data:
    for i in row:
      if i == '(':
        stack.push(i)
      elif i =='{':
        stack.push(i)  
      elif i == '[':
        stack.push(i)

      elif i == ')':
        peek = stack.peek()
        if peek =='(':
          stack.pop()
        else:
          return False
      elif i =='}':
        peek = stack.peek()
        if peek == '{':
          stack.pop()
        else:
          return False
      elif i ==']':
        peek = stack.peek()
        if peek == '[':
          stack.pop()
        else:
          return False
          
      #print(stack)
      
  pPeek = stack.peek()
  #print(Peek)
  if pPeek != "x":
    return False
  data.close()
  return True
if __name__ == '__main__':
  # The list sys.argv contains everything the user typed on the command 
  # line after the word python. For example, if the user types
  # python Delimiter_Check.py file_to_Test.py
  # then printing the contents of sys.argv shows
  # ['Delimiter_Check.py', 'file_to_Test.py']
   if len(sys.argv) < 2:
    # This means the user did not provide the filename to Test.
    # Show the correct usage.
      print('Usage: python Delimiter_Check.py file_to_Test.py')
   else:
      if delimiter_Test(sys.argv[1]):
         print('The file contains balanced delimiters.')
      else:
         print('The file contains IMBALANCED DELIMITERS.')


