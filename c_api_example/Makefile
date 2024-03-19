all: compile

compile:
	g++ -fPIC -shared $(shell python3-config --includes) -lpython3.8 fput.c -o func.so

run:
	python test.py

clean: 
	-rm -f *.so *.txt
