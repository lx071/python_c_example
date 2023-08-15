all: compile exec clean

compile:
	g++ -fPIC -shared example.cpp -o example.so

exec:
	python test.py

clean: 
	-rm -f *.so
