# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# ⋀ - and
# ⋁ - or
# ¬ - not

for x in [True,False]:
    for y in [True,False]:
        for z in [True,False]:
            resault = (not (x or y or z)) == ((not (x)) and (not (y)) and (not (z)))
            print(f'¬({x} ⋁ {y} ⋁ {z}) = ¬{x} ⋀ ¬{y} ⋀ ¬{z} = {resault}')