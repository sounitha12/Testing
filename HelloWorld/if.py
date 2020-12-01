# # hot_day1 = "It's a hot day"
# # hot_day2 = 'Drink plenty of water'
# # cold_day1 = "It's a cold day"
# # cold_day2 = 'wear warm cloths'
# # otherwise = "It's a lovely day"
# #
# # is_hot = False
# # is_cold = True
# # if is_hot:
# #     print(hot_day2)
# # elif is_cold:
# #     print(cold_day2)
# # else:
# #     print(otherwise)
# # if is_cold:
# #     print(cold_day2)
# # else:
# #      print(otherwise)
#
# good_credit = True
# x = 1000000/10
# y = 1000000/5
# if good_credit:
#     print('down payment is ' + str(x))
# else:
#     print('down payment is ' + str(y))
#
# print(f'down payment is: ${x}')

high_income = True
good_credit = False
criminal_record = True
if (high_income and not criminal_record):
    print(('eligible for loan'))
else:
    print('not eligible for loan')

temp = 30

if temp>30:
    print("it's a hot day")
elif temp<30:
    print("it's a cold day")
else:
    print("it's a lovely day")

name = "JohnjSgcssdgfjdkjsgdkcjsgdkjchgsdkfjchgdsjkbckjsdbckjsdhfjkdfjkhdjkds"
if len(name)<=4:
    print("name must be at least 3 characters")
elif len(name)>50:
    print("maximum is 50 characters")
else:
    print("name looks good")