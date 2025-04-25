from uuid import uuid4

class Avto:
    """Avtomobil klassi"""
    def __init__(self,make,model,rang,yil,narh,km=0):
        """Avtomobilning xususiyatlari"""
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narh = narh
        self.__km = km
        self.__id = uuid4()
    
    def get_km(self):
        return self.__km
    
    def get_id(self):
        return self.__id
        
avto1 = Avto()
avto1 = get_km(5)

print(get_km()) 





""" 
3-masala: Foydalanuvchi bilan ishlovchi dastur yozing
● main() funksiyasi yozing
● input() orqali foydalanuvchidan triangle yoki square kiritishini so‘rasin
● Shu nom asosida check_shape() funksiyasini chaqiring
● Natijani print() qilsin
● Dastur __name__ == "__main__" orqali ishga tushsin
"""


# class Shape:
#     def __init__(self,input_shape):
#         self.input_shape = input_shape

#     def main(self):
#         self.input_shape = input("triangle yoki square kiritishini: ")
#     def check_shape(self):
#         if self.input_shape == "triangle":
#             print("triangle shakli")
#         elif self.input_shape == "square":
#             print("square shakli")
#         else:
#             print("nomalum shakil")