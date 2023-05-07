g_num = int(input())
new_num = g_num
count = 0

while 1 :
    count += 1
    f_num = new_num // 10
    b_num = new_num % 10
    new_num = b_num*10 + ((f_num+b_num )%10)
    if g_num == new_num:
        print(count)
        break
###########################################
# # if (0 < num < 100):

# def n_saicle(num, count):
#     if num < 10:
#         num = num *10
#     count += 1
#     f_num = int(str(num)[0]) #5
#     b_num = int(str(num)[1]) #0
#     if int((str(num)[-1])) == 0:
#         num = int(str(f_num+b_num)[-1])
#     else:
#         num = int((str(num)[-1] + str(f_num+b_num)[-1])) #05
    
#     if num == g_num:
#         return 
#     n_saicle(num, count)

# n_saicle(g_num, count)

# # 55 5+5=10 :50
# # 50 5+0=5  :05
# # 05 5+0=5  :55

# # 1 1+0=1  :11

