# Makefile 
PYTHIA8=/home/chubi/Desktop/MyGit/CursoParticlePhenomenology/pythia8243
PYTHIALIB=$(PYTHIA8)/lib
PYTHIAINC=$(PYTHIA8)/include/
OBJECTS=SSTcode.o 
INCLUDE=-I$(PYTHIAINC) -I.
LDLIBS=-Wl,--no-as-needed -ldl 

SSTcode: $(OBJECTS)
	$(CXX) -o SSTcode $(OBJECTS) -L$(PYTHIALIB) -lpythia8 -lz -L$(LDLIBS)

%.o: %.cc
	$(CXX) -c $^ $(INCLUDE) -std=c++11 


