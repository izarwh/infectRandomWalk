import random
import turtle
import random
import time
import matplotlib
import numpy as np
import matplotlib.pyplot as plt

start_time = time.time()
screen = turtle.Screen()
screen.setworldcoordinates(-5, -5, 25, 30)


def animasi(xcor, ycor):

    x_max = 20
    y_max = 20
    y_min = 0
    x_min = 0
    x_range = x_max - x_min
    y_range = y_max - y_min

    # membuat grid
    grid = turtle.Turtle()
    grid.ht()
    grid.color('black')

    grid.pu()
    grid.goto(0, 0)
    grid.pd()
    grid.speed(50)

    for x in range(4):
        grid.forward(20)
        grid.left(90)

    # inisialisasi variabel
    # kondisi iterasi, berhenti apabila terjangkitCount = 0
    h = 0
    turtles = []
    haris = []
    imuns = []
    terjangkits = []
    terjangkitCount = 0
    jumlah_individu = 200
    individu_sehat = int(95/100*jumlah_individu)
    individu_terjangkit = jumlah_individu-individu_sehat

    # variable untuk dikirim ke grafik

    # instansiasi individu tidak terjangkit dengan jumlah 95% dari jumlah individu
    for j in range(individu_sehat):

        pen = turtle.Turtle()
        pen.speed(0)
        pen.shape('circle')
        pen.shapesize(0.3)
        pen.pensize(2)
        pen.color('green')

        terjangkits.append(False)
        imuns.append(False)
        haris.append(0)
        turtles.append(pen)
    # buat yang terinfeksi
    for j in range(individu_terjangkit):
        pen = turtle.Turtle()
        pen.speed(0)
        pen.shape('circle')
        pen.shapesize(0.3)
        pen.pensize(2)
        pen.color('red')
        turtles.append(pen)
        imuns.append(True)
        haris.append(0)
        terjangkits.append(True)
        terjangkitCount += 1

    # perulangan menaruh semua turtle yang telah dibuat pada posisi masing masing
    for j in range(len(turtles)):

        turtles[j].pu()
        turtles[j].ht()
        # random antara x_min hingga x_max begitu pula pada y
        turtles[j].goto(random.randrange(x_min, x_max, 1),
                        random.randrange(y_min, y_max, 1))
        turtles[j].st()
        # turtles[j].pd()

    while terjangkitCount > 0:
        for j in range(len(turtles)):

            x = turtles[j].xcor()
            y = turtles[j].ycor()

            # menggunakan method random karena rangerange berisi integer
            turn = random.random()

            # menentukan arah
            if turn <= 0.2:
                x = x + 1
            elif turn <= 0.4:
                y = y + 1
            elif turn <= 0.6:
                x = x - 1
            elif turn <= 0.8:
                y = y + 1

            if x > x_max:
                turtles[j].ht()
                turtles[j].pu()
                turtles[j].goto(x_min, y)
                x = x - x_range

            elif x < x_min:
                turtles[j].ht()
                turtles[j].pu()
                turtles[j].goto(x_max, y)
                x = x + x_range

            elif y > y_max:
                turtles[j].ht()
                turtles[j].pu()
                turtles[j].goto(x, y_min)
                y = y - y_range

            elif y < y_min:
                turtles[j].ht()
                turtles[j].pu()
                turtles[j].goto(x, y_max)
                y = y + y_range

            # infeksi
            if (turtles[j].pencolor() == 'red'):
                for k in range(len(turtles)):
                    if (((turtles[k].xcor()-turtles[j].xcor() == 0) and (turtles[k].ycor()-turtles[j].ycor() == 0)) and imuns[k] == False):
                        turtles[k].color('red')
                        terjangkits[k] = True
                        terjangkitCount += 1
                        imuns[k] = True

            # recovery time
            if (imuns[j] == True) and (terjangkits[j] == True):
                haris[j] = haris[j] + 1

            # penyembuhan
            if (haris[j] == 10 and terjangkits[j] == True):
                turtles[j].color('green')
                terjangkits[j] = False
                terjangkitCount -= 1

            turtles[j].st()
            turtles[j].goto(x, y)

        h = h+1
        ycor.append(terjangkitCount)
        xcor.append(h)

        print(terjangkitCount)


def grafik(xcor, ycor):
    plt.plot(xcor, ycor)  # -> Plot garis
    plt.title('Grafik Penyebaran Virus')
    plt.xlabel('hari')  # Sumbu -X
    plt.ylabel('jumlah terjangkit covid-19')  # Sumbu -Y
    plt.legend()
    plt.show()


xcor = []
ycor = []
animasi(xcor, ycor)
grafik(xcor, ycor)

print("time\t: %s" % (time.time() - start_time))

screen.exitonclick()
