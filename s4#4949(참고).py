## stack = FILO
while True:
    c = []
    s = list(input())
    if (len(s) == 1) and (s[0] == '.'):
        break
    else:
        for i in s:
            if (i == ')' or i== "]") and (len(c)==0):
                c.append('.')
                break
            if i == '(':
                c.append('(')
            elif i == '[':
                c.append('[')
            elif i == ')':
                if c[-1] != '(':
                    break
                else:
                    c.pop()
            elif i == ']':
                if c[-1] != '[':
                    break
                else:
                    c.pop()
        if len(c) == 0:
            print('yes')
        else:
            print('no')


################# 모범답안
# 전체적인 개념은 같지만 if문 처리가 깔끔함
# 그리고 sys는 엄청 빠르다 
# 사용하면 100ms // 안하면 360ms
import sys
input = sys.stdin.readline


while True :
    
    Char_list = list(input().rstrip()) #rstrip() 좌우 공백제거
    
    if len(Char_list) == 1 and Char_list[0] == '.' :
        break
    
    
    stack = []
    # 보안점 : 이미 위에서 input에 대한 리스트를 만들었는데
    # 다시 한번 리스트와 append를 하는 것은 효율적이지 못하다.
    for i in range(len(Char_list)) :
        if Char_list[i] == "[" :
            stack.append(Char_list[i])

        # 나는 ']' 있으면 brack 했지만, 여기서는 제거를 함
        # 만약 전에 '['가 없다면 추가를 하여서 
        # len을 늘려서 정답을 맞췄다. 
        elif Char_list[i] == "]" :
            if stack and stack[-1] == "[" :
                stack.pop()
                
            else : 
                stack.append(Char_list[i])
        
        elif Char_list[i] == "(" :
            stack.append(Char_list[i])
            
        elif Char_list[i] == ")" :
            if stack and stack[-1] == "(" :
                stack.pop()
                
            else : 
                stack.append(Char_list[i])     
        

    if len(stack) == 0 :
            print("yes")
    else :
            print("no")