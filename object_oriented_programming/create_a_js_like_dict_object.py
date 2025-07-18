class JsObject(dict):
    """A Python dictionary that provides attribute-style access
       just like a JS object:

       obj = JsObject()
       obj.cool = True
       obj.foo = 'bar'

       Try this on a regular dict and you get
       AttributeError: 'dict' object has no attribute 'foo'
    """
    def __getattr__(self, key):
        return self[key]

    def __setattr__(self, key, value):
        self[key] = value

    def __delattr__(self, item):
        self.__delitem__(item)

    def __delitem__(self, key):
        self.pop(key, None)


if __name__ == "__main__":
    D = JsObject()
    D.new_val = 5
    print(D.new_val)
    D["another_val"] = 30
    print(D["another_val"])
    del D.new_val
    print("new_val" not in D)