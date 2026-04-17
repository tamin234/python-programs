drugs_list=[2,3,56,67,7]

indx=int(input("index"))-1
for x in drugs_list:
    if drugs_list[indx]==x:
        drugs_list.pop(indx)
print(drugs_list)
  