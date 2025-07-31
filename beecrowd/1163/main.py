import math

g = 9.80665
pi = 3.14159

while True:
    try:
        altura = float(input())
        p1, p2 = list(map(int, input().split()))
        tentativas = int(input())
        for i in range(tentativas):
            angulo, velocidade = list(map(float, input().split()))
            alpha_rad = angulo * (pi / 180)
            vx = velocidade * math.cos(alpha_rad)
            vy = velocidade * math.sin(alpha_rad)
            a = -0.5 * g
            b = vy
            c = altura

            delta = b**2 - 4*a*c
            if delta < 0:
                print("O pato não atinge o solo.")
            else:
                t1 = (-b + math.sqrt(delta)) / (2*a)
                t2 = (-b - math.sqrt(delta)) / (2*a)
                tempo_queda = max(t1, t2) 
                alcance = vx * tempo_queda

                if p1 <= alcance <= p2:
                    print("{:.5f} -> DUCK".format(alcance))
                else:
                    print("{:.5f} -> NUCK".format(alcance))

    except EOFError:
        break
