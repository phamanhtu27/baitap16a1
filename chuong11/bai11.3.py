animallist=['ant','bear','cat','dog','elephant','fish','goat','hippo']
print('number of animal',len(animallist))
b=str(input('i want to find: '))
k=(b) in animallist
if k==True:
    print('there is a ',b,'in list of animal')