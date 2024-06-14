class CustomList:
    """
        __init__(self, *args): Initialize the custom list with an arbitrary number of arguments.
        __repr__(self): Return a string representation of the custom list.
        __len__(self): Return the length of the custom list.
        __getitem__(self, index): Retrieve an item at a specific index.
        __setitem__(self, index, value): Set the value of an item at a specific index.
        __delitem__(self, index): Delete an item at a specific index.
        __iter__(self): Return an iterator for the custom list.
        __contains__(self, item): Check if an item is in the custom list.
        __add__(self, other): Concatenate another custom list or a Python list to the custom list.
        __iadd__(self, other): Implement the in-place addition.
        __str__(self): Return a user-friendly string representation of the custom list.
    """
    def __init__(self, *args):
        self.list = list(args)

    def __repr__(self):
        return f"CustomList({self.list})"

    def __len__(self):
        return len(self.list)
    
    def __getitem__(self, index):
        return self.list[index]
    
    def __setitem__(self, index, value):
        self.list[index] = value
    
    def __delitem__(self, index):
        del self.list[index]

    def __iter__(self):
        return iter(self.list)
    
    def __contains__(self):
        pass
    
    def __add__(self, other):
        if isinstance(other, CustomList):
            return CustomList(*(self.list + other.list))
        elif isinstance(other, list):
            return CustomList(*(self.list + other))
        else:
            raise TypeError("Unsupported operand type(s) for +: 'CustomList' and '{}'".format(type(other).__name__))

    
    def __iadd__(self, *args):
        pass
    
    def __str__(self, *args):
        return str(self.list)

if __name__ == '__main__':
    custom_list = CustomList(1, 2, 3)
    print(custom_list)
    print(repr(custom_list))