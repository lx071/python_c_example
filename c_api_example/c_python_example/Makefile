all: compile

compile:
	g++ -fpie $(shell python3-config --cflags --embed) -o test 01.cpp $(shell python3-config --embed --ldflags) 

run:
	./test

clean: 
	-rm -rf test
