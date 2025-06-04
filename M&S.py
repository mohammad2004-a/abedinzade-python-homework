def main():
    list = []
    while True:
        b = int(input("Enter number : "))
        list.append(b)
        if len(list)>3:
            print("continiue ?")
            if input() == "n":
                break
            else:None
    print(get_maximum(list))
    print(sort(list))        
        
                  
def get_maximum(list) -> int:
    maximum = list[0]
    
    for i in range(1,len(list)) :
        if maximum < list[i]:
            maximum = list[i] 
    return maximum        
                
                          
def sort(list):
    for i in range(len(list)):
        for j in range( i+1 ,len(list)):
            # اینجوری دیگه با خودش مقایسه نمی کنه
            if list[i] > list[j]:
                list[i],list[j]=list[j],list[i]
    return list                                 
    

main() 
