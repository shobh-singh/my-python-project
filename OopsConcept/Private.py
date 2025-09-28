# class private1:
#     __accpass=343    #double underscore

# s1=private1()
# print(s1.__accpass)  #Doesnot access




class account:
    def __hello(self):    #private method doble underscore
        print("hello person")

    def A(self):
        self.__hello()
s1=account()
s1.A()
   

         

