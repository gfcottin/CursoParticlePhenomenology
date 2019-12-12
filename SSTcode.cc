#include "Pythia8/Pythia.h"
#include <vector>
#include <string>
#include <iterator>
#include <algorithm>

using namespace Pythia8;

int main() {

  // You can always read an plain LHE file,
  // but if you ran "./configure --with-gzip" before "make"
  // then you can also read a gzipped LHE file.
  #ifdef GZIPSUPPORT
    bool useGzip = true;
  #else
    bool useGzip = false;
  #endif
    cout << " useGzip = " << useGzip << endl;

  Pythia pythia;
  Event& event = pythia.event;

  // Initialize Les Houches Event File run. List initialization information.
  pythia.readString("Beams:frameType = 4");
  pythia.readString("Beams:LHEF =/home/chubi/Desktop/MyGit/CursoParticlePhenomenology/MG5_aMC_v2_4_3/SST_GRID_e/SST_GRID_e-50/Events/run_01/unweighted_events.lhe.gz");
 
  int nEvent = 10000;//FROM LHE File
  int nAbort = 50;   

  ////// Initialize.
  pythia.init();
  Hist mult("charged multiplicity", 100, -0.5, 799.5);

  //Files
  ofstream electrons;
  electrons.open("electrons.dat"); 
  ofstream neutrinos;
  neutrinos.open("neutrinos.dat"); 
  
  int iAbort = 0;
  int nPromptElectron=0;


  // Begin event loop; generate until none left in input file.
  for (int iEvent = 0; ; ++iEvent) {
  cout << "######## Event "<<iEvent<<" #########"<<endl;
  // for (int iEvent = 0; iEvent < nEvent; ++iEvent) {
    // Generate events, and check whether generation failed.
    if (!pythia.next()) {
      // If failure because reached end of file then exit event loop.
      if (pythia.info.atEndOfFile()) break;
      // First few failures write off as "acceptable" errors, then quit.
      if (++iAbort < nAbort) continue;
      break;
    }

    bool passEvtPromptElectron  = false; 
    std::vector<double> electronpT;
    ///////////////////
    // Electron trigger
    ///////////////////
    for (int i= 0; i < event.size(); i++){
      if (abs(event[i].id()) == 11){

        cout<<"there is an electron"<<endl;
        cout<<event[i].pT()<<endl;

        // Apply electron efficiency for detector effect
        // float iRndNumber = (std::rand()/(float)RAND_MAX); 
        // cout<<"iRndNumber = "<<iRndNumber<<endl;
        // passElecEff = 0.8 >iRndNumber;
        
        if((event[i].pT()>10.) && abs(event[i].eta())<2.4) {
          passEvtPromptElectron=true;
          electrons<<event[i].pT()<<endl;
        }
      }
    }
    if(passEvtPromptElectron) nPromptElectron++;
    //if(passEvtPromptElectron && passElecEff) nPromptElectron++;
      else continue; //    std::vector<int> motherIndices;   
    
    //Get neutrinos from event
    for (int i= 0; i < event.size(); i++){
      if (abs(event[i].id()) == 112){

        cout<<"there is a neutrino"<<endl;
        
        double p = sqrt(pow2(event[i].px())+pow2(event[i].py())+pow2(event[i].pz()));
        double mass = event[i].m();
        double gamma = p/mass;
        //motherIndices.push_back(i);
        neutrinos<<mass<<" "<<gamma<<" "<<event[i].pT()<<endl;  
        }
      }    

    // Find charged particles from the event. (How many are coming from the neutrino?)
    int nCharged = 0;
    for (int i= 0; i < event.size(); i++){
      if (pythia.event[i].isFinal() && pythia.event[i].isCharged())
        ++nCharged;
    mult.fill( nCharged );

    }  

  }//End of event loop.    

  cout <<" CutFlow for mN [GeV]  = "<< setprecision(5)<< pythia.particleData.m0(112) <<endl;
  cout <<" All events     "      << nEvent                << " " << nEvent*100./nEvent            << " " << nEvent*100./nEvent    << endl;
  cout <<" Prompt lepton  "      << nPromptElectron       << " " << nPromptElectron*100./nEvent   << " " << nPromptElectron*100./nEvent<< endl;
 
  neutrinos.close();
  electrons.close();
  return 0;
}