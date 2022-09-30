str ="(()[({})]){[[()]]}))" #input("enter a text with brackets")

def checkBalnced(str):
    arr=[]
    j= -1
    for i in str:
        if(i=="("):
            arr.append(i)
            j+=1
        elif(i==")"):
            if(len(arr)!=0 and arr[j] == "("):
                arr.pop()
                j-=1
            else:
                return "not balanced"
        elif(i=="["):
            arr.append(i)
            j+=1
        elif(i=="]"):
            if(len(arr)!=0 and arr[j] == "["):
                arr.pop()
                j-=1
            else:
                return "not balanced"
        elif(i=="{"):
            arr.append(i)
            j+=1
        elif(i=="}"):
            if(len(arr)!=0 and arr[j] == "{"):
                arr.pop()
                j-=1
            else:
                return "not balanced"   
    if(len(arr)==0):
        return "balnced"
    else:
        return "not balanced"
print(checkBalnced(str))