class ListNode:
    def __init__(self,val):
        self.val = val
        self.nxt = None
    
class MyHashSet:

    def __init__(self):
        self.size = 3313
        self.bucket = []

        for i in range(self.size):
            self.bucket.append(ListNode(-1))
    
    def _insert(self,idx,key):
        head = self.bucket[idx]
        
        if self._search(idx,key):
            return
        
        node = ListNode(key)
        
        ref = head.nxt
        head.nxt = node
        node.nxt = ref

    def add(self, key: int) -> None:
        idx = key%self.size
        self._insert(idx,key)    

    def _remove(self,idx,key):
        node = self.bucket[idx]
        pre = None

        while node:
            if node.val==key:
                break
            pre = node
            node = node.nxt

        if node:
            pre.nxt = node.nxt

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