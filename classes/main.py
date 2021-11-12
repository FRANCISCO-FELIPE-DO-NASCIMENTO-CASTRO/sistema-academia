class Spooler(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Spooler, cls).__new__(cls)

        return cls.instance





s = Spooler()
s1 = Spooler()
s3 = Spooler()

print(s)
print(s1)
print(s3)