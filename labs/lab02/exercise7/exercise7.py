def check_collision(x1, y1, w1, h1, x2, y2, w2, h2):
    return (x1 > x2 and y1 > y2) or (x1 < x2 and y1 < y2) or (w1 < w2 and h1 < h2) or  (w1 > w2 and h1 < h2)


print(check_collision(2,4,5,8,12,6,2,5))