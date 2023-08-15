all: compile

compile:
	g++ main.cpp $(shell python3 -m pybind11 --includes) -lpython3.8 -o hello

run:
	./hello
	
clean:
	-rm -rf __pycache__ hello
