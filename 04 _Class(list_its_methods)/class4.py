#    ->                   0       1       2
#names  : list[str] = ["Qasim", "Sir Zia", "Sir Inam", 123] # here it don't show error we need to put in py file
#   <-                    -1      -2      -1

#print(names[-2])


from typing import Any
                   #    0           1      2
names : list[Any] = ["Am Cucum" , "saad" ,"TQ "]
         #               -3          -2       -1
print(names[1])



names2 : list[Any] = ["Am Cucum" , "saad" ,"TQ "]
         #               -3          -2       -1
print(f" {names[1]}")


characters : list[str] = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
print(characters)