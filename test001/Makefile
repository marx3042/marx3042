CC = gcc
<<<<<<< HEAD
all: main

main: test001.o func.o
	$(CC) -o main test001.o func.o
test001.o: test001.c header.h
	$(CC) -c test001.c
func.o: func.c header.h
	$(CC) -c func.c
clean:
	rm -rf main *.o
=======

all: main

main : main.o func.o
	$(CC) -o main main.o func.o
main.o: main.c header.h
	$(CC) -c main.c
func.o: func.o header.h
	$(CC) -c func.c
clean:
	rm -rf main *.o
>>>>>>> fb53898d8830fb2b0ade49a3d273c245c1c4e9ff
