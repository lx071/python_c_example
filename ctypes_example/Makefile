all: compile

compile:
	g++ -fPIC -shared example.cpp -o example.so

run:
	python test.py

clean: 
	-rm -f *.so
