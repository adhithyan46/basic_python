# car={
#     "brand":"maruti",
#     "model":"alto",
#     "year":1960
# }
# x=car.get("brand")
# x=car.keys()
# x=car.values()

# print(x)

# car["model"]="swift"
# x=car.items()
# print(x)

# car={
#     "brand":"maruti",
#     "model":"alto",
#     "year":1960,
#     "model":"toyota"
# }
# x=car.keys()
# car["color"]="blue"
# print(car)
# print(len(car))
# print(type(car))
# x=car.get("model")
# car["model"]="swift"
# car.update({"model":"swift"})
# car.pop("year")
#car.popitem()
# del car["model"]
# del car
# car.clear()
# print(car)

car={
    "brand":"maruti",
    "model":"alto",
    "year":1960,
    "model":"toyota"
}
# for i in car:
#     print(car[i])
# for i in car:
#     print(i)
# for i in car.keys():
#     print(i)
# for x,y in car.items():
#     print(x,y)
# car2=car.copy()

car2=dict(car)
print(car2)
