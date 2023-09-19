CC = gcc
all: main

main: test001.o func.o
	$(CC) -o main test001.o func.o
test001.o: test001.c header.h
	$(CC) -c test001.c
func.o: func.c header.h
	$(CC) -c func.c
clean:
	rm -rf main *.o