st=input("Enter a word  ")
st2=""
for i in st:
    st2=i+st2
print("Orignal word is ",st)
print("Reversed word is ",st2)
if st==st2:
    print("It is a palendrome")
else:
    print("It is not a palendrome")