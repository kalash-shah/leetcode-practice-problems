x = int(input("Enter a number: "))
my_num = x
reverse_num = 0
while my_num > 0:
    dig = my_num%10
    reverse_num = reverse_num*10+dig
    my_num = my_num // 10
if reverse_num == x:
    print("true")
else:
    print("false") 