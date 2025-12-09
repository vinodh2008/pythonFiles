# #even or odd
# int(input("enter a number:"))
# if number%2:
#     print("even number")    
# else:
#     # print("odd number")
# this program is used to do the validatation
# take the password if that password entered by user is valid means its satisfies the     requirements
special="@#$%^&*()!`~"
special_count=0
upper_count=0
num_count=0
uppercase="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers="0123456789"
while(1):
    password=input("enter the password")
    if len(password)>=8 and len(password)<=16:
        for i in password:
            if i in special:
                special_count=special_count+1
                # print(special_count)
                
            if  i in uppercase:
                upper_count=upper_count+1
                # print(i)
            if  i in numbers:
                num_count=num_count+1
                # print(i)
        if special_count<=0:
            print("enter one special character at least")
            break
        if upper_count<=0:
            print("require minimum one upper character in password")
            break 
        if num_count<=3:
            print("require the more than three numbers in password")
            break
        
        print("your entered password is ",password)
        break
        
    else :
        print("password lenght is greater than 8 and less than equal to  16 ")
        break

            
            