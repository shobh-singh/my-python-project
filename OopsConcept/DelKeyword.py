class Del:
    def __init__(self, name):
        self.name=name

s1=Del("Vikram")
print(s1.name)

del s1.name

print(s1.name)