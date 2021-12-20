class dictionary:
    def __enter__(self):
        dict = self.dict = [1, 2, 3, 4, 5, {1: "unu",
                                            2: "doi",
                                            3: "trei"}]
        return self.dict

    def just_some_exceptions(self):
        try:
            print(dict)
        except IndexError:
            print('Nu exista index')
        except KeyError:
            print('Nu exista cheie')
        return dict

    def __exit__(self, exc_value, exc_type, traceback):
        if exc_value is IndexError:
            print('Nu exista INDEX')
        elif exc_value is KeyError:
            print('Nu exista KEY')
        return True

with dictionary() as dictionn :
    print(dictionn[5][5])
    
with dictionary() as dictionn:
    print(dictionn[7])
