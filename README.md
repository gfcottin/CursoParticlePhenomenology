# CursoParticlePhenomenology

## HEP Software ##

The following software must be installed for the curse :

  * A good text editor ! I recommend [Sublime](https://www.sublimetext.com/3)	
  * python
  * [MadGraph](https://launchpad.net/mg5amcnlo)
  * [FastJet](http://fastjet.fr/quickstart.html)
  * [Pythia8](http://home.thep.lu.se/Pythia/) (compiled with gzip, FastJet)
  * [ROOT](https://root.cern.ch/)  
  * [Delphes](https://cp3.irmp.ucl.ac.be/projects/delphes)

## MadGraph ##

Go to launchpad and do:

tar -xzf MG5_aMC_v2.X.X.tar.gz

cd MG5_aMC_v2_3_0

./bin/mg5_aMC

tutorial

Follow tutorial:

generate p p > t t~

display processes

display diagrams

output MY_FIRST_MG5_RUN

launch

0

Open MY_FIRST_MG5_RUN and analyse folder, but leave tutorial terminal open.

Following the tutorial again until finish.


## Exercise 1:##

Plot the cross-section of the right-handed neutrino vs its mass for the the type-I see-saw model

(import SST model
modify run_card for 1000 events
run scripted SST run)

Now, generate a grid of masses with the python script and run an scripted run for all masses
## Fastjet ##

curl -O http://fastjet.fr/repo/fastjet-3.3.3.tar.gz

tar zxvf fastjet-3.3.3.tar.gz

cd fastjet-3.3.3/

./configure --prefix=$PWD/../fastjet-install

make

make check

make install

cd ..

And then follow example on the website.

## Pythia ##

Download Pythia8

tar xvfz pythia8243.tgz

./configure --with-gzip --with-fastjet3=/home/gfcottin/fastjet-install

make
