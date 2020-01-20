#WHILE

it = 10
while it>1:
    if it == 3:
#break statement
        break           #break will break the whole loop
    print(it)

    it = it - 1              #to stop the infinite looping

print("while loop execution is done")
it1=10
while it1>1:
    if it1 == 9:
        it1=it1-1
        continue
    if it1 ==3:
        break
    print(it1)

    it1=it1 - 1

