#this is my green bottle code########
bottles=10
for x in range(bottles,0,-1):
    print("{0} green bottle hanging on the wall.\n{0} green bottles hanging on the wall.".format(x))
    print("And if 1 green bottle should acidentally fall, \nThere'll be {0} green bottles hanging on the wall.\n".format(x-1))
