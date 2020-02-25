# url: https://www.hackerrank.com/challenges/30-queues-stacks/problem
# 문제가 좋아서 저장해둠.

import sys


class Solution:
    # Write your code here
    stack = []
    queue = []

    def pushCharacter(self, character):
        self.stack.append(character)

    def popCharacter(self):
        return self.stack.pop()

    def enqueueCharacter(self, character):
        self.queue.append(character)

    def dequeueCharacter(self):
        char = self.queue[0]
        del self.queue[0]
        return char


# read the string s
s = input()
# Create the Solution class object
obj = Solution()

l = len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

isPalindrome = True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
'''
for i in range(l // 2):
    if obj.popCharacter() != obj.dequeueCharacter():
        isPalindrome = False
        break
# finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, " + s + ", is a palindrome.")
else:
    print("The word, " + s + ", is not a palindrome.")