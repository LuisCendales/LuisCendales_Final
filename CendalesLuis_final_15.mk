CendalesLuis_final_15.png: lista.dat plot.py
    python plot.py

lista.dat : a.out
    ./a.out 

a.out: calculo.cpp
    g++ calculo.cpp
