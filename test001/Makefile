CC = gcc

all: main

main : main.o func.o
	$(CC) -o main main.o func.o
main.o: main.c header.h
	$(CC) -c main.c
func.o: func.o header.h
	$(CC) -c func.c
clean:
	rm -rf main *.o
