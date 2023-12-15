def f(x):
    return (2*x**2 - 5*x + 3)


x = 0

for i in range(1, 101):
    new_x = x - f(x)/(4*x-5)
    
    if abs(new_x - x) < 0.000001:
        break
        
    x = new_x
    
print(f"Miejsce zerowe w x = {new_x:.2f} znalezione w {i} iteracjach")