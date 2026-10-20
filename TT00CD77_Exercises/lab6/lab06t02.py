def celToFah(x):
    final=((x*1.8)+32)
    return round(final, 1)
def fahToCel(x):
    final=((x-32)/1.8)
    return round(final, 1)
print(celToFah(10.0))
print(fahToCel(38.0))