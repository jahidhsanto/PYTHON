# SYNTAX
# [expression for item in list]

num = [1, 2, 3, 4, 5]

#################################################
result = list(map(lambda x: x*x, num))        #
print(result)                                   #
                                                #
# Convert this to List_Comprehensions           #
                                                #
result = [x*x for x in num]                     #
print(result)                                   #
#################################################

#################################################
result = list(filter(lambda x: x%2==0, num))    #
print(result)                                   #
                                                #
# Convert this to List_Comprehensions           #
                                                #
result = [x for x in num if x%2==0]             #
print(result)                                   #
#################################################
