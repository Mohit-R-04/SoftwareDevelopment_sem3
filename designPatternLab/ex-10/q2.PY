def sorting(lst):
    return sorted(lst)

def getval(lst, index):
    if index < len(lst):
        return lst[index]
    else:
        return None

class NDArrayAdapter:
    def __init__(self, ndarray):
        self.flat_list = self.flatten(ndarray)
    
    def flatten(self, ndarray):
        if isinstance(ndarray, (list, tuple)):
            flat_list = []
            for item in ndarray:
                flat_list.extend(self.flatten(item))
            return flat_list
        else:
            return [ndarray]
    
    def sort(self):
        self.flat_list = sorting(self.flat_list)
    
    def get_value(self, index):
        return getval(self.flat_list, index)

nd_array = [[3, 1], [4, 2],[5,0]]
adapter = NDArrayAdapter(nd_array)

# Flatten and sort
adapter.sort()
print(adapter.flat_list)  # Output: [1, 2, 3, 4]

# Get value at index
print(adapter.get_value(2))  # Output: 3
