def brightness_check(bright):
    count = 0
    for i in range(len(bright)):
        for j in range(len(bright)):
            if bright[i] == bright[j] or i != j+1:
                continue
            elif bright[i] > bright[j] and bright[i] > bright[j+2]:
                print(f"Index {i}: brighter than neighbors → Bright spot")
                count += 1
    print("Count =", count)
    
Pixels = [100, 120, 200, 150, 180, 160, 140]
brightness_check(Pixels)


















