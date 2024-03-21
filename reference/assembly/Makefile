CC = g++

TARGET = app

CFLAGS = -std=c++17 -Wall

all: $(TARGET)

$(TARGET): main.cpp
	$(CC) $(CFLAGS) -o $(TARGET) main.c

clean:
	$(RM) $(TARGET)

assembly:
	gcc -S -o test.s main.c
