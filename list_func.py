# list_in=(input("Enter the list(seperate via spaces) ")).split( )
# new=(input("enter the new num to be inserted"))
# list_in.append(new)
# print(list_in)
# if len(list_in)>0:
#     list_in.pop(0)
# print(list_in[: : -1])



# list_in = [x**2 for x in range(1,20)]
# print(list_in)


# Step 1: Initial list input
lizt = input("Enter the elements with spaces: ").split()
conv = [eval(item) for item in lizt]

# Step 2: Extra input
extra = input("Enter the elements to be inserted: ").split()
convr = [eval(item) for item in extra]

# Step 3: Extend the original list
conv.extend(convr)  # or: conv += convr

# Step 4: Output
print("Updated list:", conv)
