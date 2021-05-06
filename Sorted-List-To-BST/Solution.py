# Definition for singly-linked list.
class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next
# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right
class Solution:
	
	def sortedListToBST(self, head):
		
		if not head:
			return head
		
		mid = self.getMid(head)
		root = TreeNode(mid.val)
		
		if head!= mid:
			root.left = self.sortedListToBST(mid.next)
			root.right = self.sortedListToBST(head)
		
		return root
	
	def getMid(self, head):
		
		slow = head
		fast = head
		prev = head

		while fast != None and fast.next!=None:
			prev = slow
			slow = slow.next
			fast = fast.next.next
		
		prev.next = None
		return slow


root = ListNode(-10)
head = root
ele = [-3,0,5,9]

for e in ele:

	node = ListNode(e)
	root.next = node
	root = root.next

s = Solution()
s.sortedListToBST(head)
		
		