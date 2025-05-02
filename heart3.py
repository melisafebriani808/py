import turtle
import time

# Setup layar
screen = turtle.Screen()
screen.bgcolor("black")

# Turtle untuk menggambar outline hati (sekali saja)
outline = turtle.Turtle()
outline.penup()
outline.goto(0, -100)
outline.pendown()
outline.color("pink")
outline.pensize(3)
outline.speed(1)

# Gambar outline hati satu kali
outline.begin_fill()
outline.setheading(140)
outline.forward(180)
outline.circle(-90, 200)
outline.left(120)
outline.circle(-90, 200)
outline.forward(180)
outline.end_fill()
outline.hideturtle()

# Turtle untuk isi love yang akan kelap-kelip
fill = turtle.Turtle()
fill.penup()
fill.goto(0, -100)
fill.pendown()
fill.speed(0)
fill.hideturtle()

# Daftar warna kelap-kelip
colors = ["black", "pink"]

# Fungsi untuk mengisi hati tanpa menghapus bentuk
def fill_heart(color):
    fill.color(color)
    fill.begin_fill()
    fill.setheading(140)
    fill.forward(180)
    fill.circle(-90, 200)
    fill.left(120)
    fill.circle(-90, 200)
    fill.forward(180)
    fill.end_fill()

# Animasi warna isi hati (tanpa hapus bentuk)
for _ in range(8):
    for color in colors:
        fill.clear()
        fill_heart(color)
        time.sleep(0.5)

# Selesai
turtle.done()
