def main():
    ...

class Jar:
    #the Init creates a Jar object given a capacity, by default it's 12.
    def __init__(self, capacity=12):
        #if the capacity is not a positive integer it raises a value error
        if capacity < 0:
            raise ValueError

        self.max_capacity = capacity
        self.cookies = 0

    #We return the quantity of cookies in the jar printing 🍪 for each cookie.
    def __str__(self):
        return "🍪" * self.cookies

    #If adding n cookies to the jar excess the capacity of the jar it raises a ValueError.
    def deposit(self, n):
        if (self.cookies + n) > self.max_capacity:
            raise ValueError
        else:
            self.cookies += n
    #If subtracting n cookies from the jar exceeds the number of cookies in the jar a ValueError is raised.
    def withdraw(self, n):
        if (self.cookies - n) < 0:
            raise ValueError
        else:
            self.cookies -= n

    @property
    def capacity(self):
        return self.max_capacity

    @property
    def size(self):
        return self.cookies

if __name__ == "__main__":
    main()
