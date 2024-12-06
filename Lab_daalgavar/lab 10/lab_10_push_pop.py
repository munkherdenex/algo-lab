class StackWithBackup:
    def __init__(self, k):
        self.stack = []
        self.k = k
        self.operation_count = 0 
        self.total_cost = 0       
        self.backup_cost = 0     

    def push(self, x):

        self.stack.append(x)
        self.operation_count += 1
        self.total_cost += 1 

        if self.operation_count % self.k == 0:
            self._backup()

    def pop(self):

        if not self.stack:
            raise IndexError("hooson stack-s pop.")
        
        self.stack.pop()
        self.operation_count += 1
        self.total_cost += 1  

        if self.operation_count % self.k == 0:
            self._backup()

    def _backup(self):

        self.backup_cost += len(self.stack)  
        self.total_cost += len(self.stack)  

    def get_total_cost(self):

        return self.total_cost

    def get_backup_cost(self):

        return self.backup_cost


k = 5 
stack = StackWithBackup(k)

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)  
stack.pop()
stack.push(6)
stack.push(7)
stack.pop()   

print("Niit zardal:", stack.get_total_cost())
print("Niit Backup zardal:", stack.get_backup_cost())
