class person:
    name="vikram"

    @classmethod
    def changename(cls , name):
        cls.name=name

c1=person()
c1.changename("vikram")
print(c1.name)
print(person.name)

