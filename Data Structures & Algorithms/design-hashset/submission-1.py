class ListNode:
    def __init__(self,val):
        self.val = val
        self.pre = None
        self.nxt = None
    
class MyHashSet:

    def __init__(self):
        self.size = 3313
        self.bucket = [None]*self.size
    
    def _insert(self,idx,key):
        if self.bucket[idx] is None:
            head = ListNode(-1)
            tail = ListNode(-1)
            head.nxt,tail.pre = tail,head
        else:
            head = self.bucket[idx]
        
        node = ListNode(key)

        if self._search(idx,key):
            return
        
        # insert
        ref = head.nxt
        head.nxt = node
        node.pre = head
        node.nxt = ref
        ref.pre = node

        if self.bucket[idx] is None:
            self.bucket[idx] = head

    def add(self, key: int) -> None:
        idx = key%self.size
        self._insert(idx,key)    

    def _remove(self,idx,key):
        head = self.bucket[idx]
        node = head

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

        self.bucket[idx] = head

    def remove(self, key: int) -> None:
        idx = key%self.size
        self._remove(idx,key)
    
    def _search(self,idx,key):
        head = self.bucket[idx]
        if head is None:
            return False

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