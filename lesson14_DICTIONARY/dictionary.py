





# ! DICTIONARIES
#   key + value


# months = {
#     "january" : 31,
#     "february" : 28,
#     "march" : 30,
#     "april" : 31,
#     "june" : 30, 
#     "july" : 31,
#     "august" : 31,
#     "september" : 30,
#     "october" : 31,
#     "november" : 30,
#     "december" : 31,
# }

# print(months["july"])




# calc = {
#     "add":  "+"  ,
#     "subtract": "-" , 
#     "multiply" :  "*" ,
#     "divide" :  "/"
# }
# def cal_num(num1, num2, action ):
#     return eval(f"{num1}{calc[action]}{num2}")   
# print(cal_num(2, 5, "divide"))    
    




english ={
            1 : "aeioulnstr",
            2 : "dg",
            3 : "bcmp",
            4 : "fhvwy",
            5 : "k",
            8 : "jx",
            10 : "qz"}
russian = {
            1 : "авеинорст", 
            2 : "дклмпу",
            3 : "бгёья",
            4 : "йы",
            5 : "жзхцч",
            8 : "шэю",
            10 : "фщъ"}
import re
def is_cyrillic(text):
    return bool(re.search("[а-яА-Я]", text))
text = input().lower()
if is_cyrillic(text):
    print(sum([k for i in text for k, v in english.items()]))






