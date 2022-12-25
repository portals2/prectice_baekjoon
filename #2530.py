# h_, m_, s_= input().split(' ')
# time = int(input())

# h = 0
# m = time // 60
# s = time - m * 60

# h_ = int(h_)
# m_ = int(m_)
# s_ = int(s_)

# c_s = 0
# c_m = 0

# if (s + s_) > 59:
#     s_s = (s + s_) // 60
#     m += s_s
#     c_s = (s + s_) - (s_s * 60)

# if (m + m_) > 59:
#     m_m = (m + m_) // 60
#     h += m_m
#     c_m = (m + m_) - (m_m * 60)

# if (h + h_) < 24:
#     if (s + s_) < 59:
#         if (m + m_) < 59:
#             print(h + h_, m + m_, s + s_)
#         else:
#             print(h + h_, c_m, s + s_)
#     else:
#         if (m + m_) < 59:
#             print(h + h_, m + m_, c_s)
#         else:
#             print(h + h_, c_m, c_s)          
# else:
#     if (s + s_) < 59:
#         if (m + m_) < 59:
#             print(h + h_, m + m_, s + s_)
#         else:
#             print(h + h_, c_m, s + s_)
#     else:
#         if (m + m_) < 59:
#             print((h + h_)-24, m + m_, c_s)
#         else:
#             print((h + h_)-24, c_m, c_s)

h,m,s = map(int,input().split(" "))
sec = int(input())

# h:시각, m:분, s:초, sec:추가된 초
#고려요소 1번째
s1 = (s+sec)%60  #최종 초
m1 = (s+sec)//60
#고려요소 2번째
m2 = (m+m1)%60 # 최종 분
h1 = (m+m1)//60
#고려요소 3번째
h2 = (h+h1)%24 # 최종 시각

print(h2,m2,s1)  #출력