
class TypeHandling:
    def init(self):
        pass

    def type_fixer(self,qxn,doc):
        if qxn['type'] == "int":
            try:
                doc[qxn['key']] = int(doc[qxn['key']])
            except:
                raise TypeError("not an integer")
        elif qxn['type'] == "tuple":
            try:
                X, Y = doc[qxn['key']].split(",")
                doc[qxn['key']] = (int(X), int(Y))
            except:
                raise TypeError("not a tuple")
        elif qxn['type'] == "str":
            doc[qxn['key']] = str(doc[qxn['key']])
        return doc
    