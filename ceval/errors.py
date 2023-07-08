
class UniqueNameError(Exception):

    def __init__(self, name_1, name_2):
        self.message = "name "+str(name_1)+" is the same with the name "+str(name_2)
        super().__init__(self.message)

