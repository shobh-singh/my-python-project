class A:
    def show(self):
        try:
            10/2

        except Exception:

            print("Error Not Divide By Zero")

        else:
            print("Divide By Zero")

        finally:
            print("Completed Code !!")    

        

c1=A()
c1.show()
    