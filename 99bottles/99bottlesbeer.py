for i in range(99, 0, -1):
    if i == 1:
        print("1 bottle of beer on the wall, 1 bottle of beer!")
        print("So take it down, pass it around, no more bottles of beer on the wall!")
    elif i == 2:
        print("2 bottles of beer on the wall, 2 bottles of beer!")
        print("So take one down, pass it around, 1 bottle of beer on the wall!")
    else:
        print(f"{i} bottles of beer on the wall, {i} bottles of beer!")
        print(f"So take one down, pass it around, {i-1} bottles of beer on the wall!")

if i == 1:
    print("And then all of the beers came crashing down!")
