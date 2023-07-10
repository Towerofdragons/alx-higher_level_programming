#/usr/bin/python3
""" MODULE holds definition for MyLst class """


class MyList(list):
    """
    Defines a subclass for 'List' inheriting from the list class.
    """
    def print_sorted(self):
        print("{}".format(sorted(self)))
