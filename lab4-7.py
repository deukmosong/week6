def circle_area_circum(radius):
    area=radius*radius*3.14
    circum=2*3.14*radius
    return area ,circum

radius=10

area ,circum=circle_area_circum(radius)

area=round(area,1)
circum=round(circum,1)

print('반지름 ',radius,'인 원의 면적은 ',area,'원의 둘레는',circum)