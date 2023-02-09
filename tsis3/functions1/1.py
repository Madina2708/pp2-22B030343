def g_to_o(weight):
    new_weight = weight / 28.3495
    return new_weight

weightgrams = 777

weight_in_onces = g_to_o(weightgrams)

print(f"{weight_in_onces} g")