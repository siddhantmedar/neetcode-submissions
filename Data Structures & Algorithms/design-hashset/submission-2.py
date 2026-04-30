class ListNode:
    def __init__(self,val):
        self.val = val
        self.pre = None
        self.nxt = None
    
class MyHashSet:

    def __init__(self):
        self.size = 3313
        self.bucket = []

        for i in range(self.size):
            head = ListNode(-1)
            tail = ListNode(-1)
            
            head.nxt,tail.pre = tail,head

            self.bucket.append(head)
    
    def _insert(self,idx,key):
        head = self.bucket[idx]
        
        # dont allow duplicates to be added
        if self._search(idx,key):
            return
        
        node = ListNode(key)
        
        # insert
        ref = head.nxt

        head.nxt = node
        node.pre = head
        node.nxt = ref
        ref.pre = node

    def add(self, key: int) -> None:
        idx = key%self.size
        self._insert(idx,key)    

    def _remove(self,idx,key):
        node = self.bucket[idx]

        if node is None:
            return

        while node:
            if node.val==key:
                break
            node = node.nxt

        if node:
            pre,nxt = node.pre, node.nxt
            pre.nxt = nxt
            nxt.pre = pre

    def remove(self, key: int) -> None:
        idx = key%self.size
        self._remove(idx,key)
    
    def _search(self,idx,key):
        head = self.bucket[idx]

        while head:
            if head.val==key:
                return True
            head = head.nxt

        return False

    def contains(self, key: int) -> bool:
        idx = key%self.size
        return self._search(idx,key)

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)