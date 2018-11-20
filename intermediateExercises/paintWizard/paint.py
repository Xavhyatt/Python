

def total_cost(paint, coverage):
    volume_of_paint = coverage/paint.get("coverage_per_litre")
    print(volume_of_paint)
    number_of_cans = volume_of_paint/paint.get("size")
    print(number_of_cans)

    if (number_of_cans).is_integer()==True:
        print(number_of_cans)
        total_cost = number_of_cans * paint.get("price")
        return  total_cost

    else:
        total_cost = (int(number_of_cans) + 1) * paint.get("price")
        print(number_of_cans)
        return total_cost


def left_over(paint, coverage):
    volume_of_paint = coverage/coverage_per_litre
    number_of_cans = volume_of_paint / size

    if (number_of_cans).is_integer()==True:
        left_over = (number_of_cans * size) - volume_of_paint
        return left_over

    else:
        left_over = ((int(number_of_cans) + 1) * size) - volume_of_paint
        return left_over


average_joe = {
    "price" : 17.99,
    "size" : 15,
    "coverage_per_litre" : 11
}

cheapo = {
    "price" : 19.99,
    "size" : 10,
    "coverage_per_litre" : 10
}

dulux = {
    "price" : 25,
    "size" : 10,
    "coverage_per_litre" : 20
}

print(total_cost(dulux, 200))