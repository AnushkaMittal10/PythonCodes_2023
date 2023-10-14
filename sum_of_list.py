def add(items):
    x = 0
    for item in items:
        x = x+item;
    return x
enter_list = input("Enter your list as (1,2,x...):").split(",")
map_int = map(int, enter_list)
print(add(map_int))