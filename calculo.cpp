#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

int main(){
    double t=0.;
    double tf=10.;
    double deltat =0.1;
    
    int posx=1;
    int posy=0;
    
    double velx=0;
    double vely=1;
    
    double ax=0;
    double ay=0;
    
    double m= 7294.29;
    int q=2;
    ofstream outfile;
    
    
    outfile.open("lista.dat")
    for(int i=0;i<101;1++){
        outfile << t << "" << posx << " " << posy ;
        posx = posx + velx*deltat;
        posy = posy + vely*deltat;
        velx = velx + ax*deltat;
        vely = vely + ay*deltat;
        if(i>29){
            ay=3
        }else if(1<71){
            ay=3
        }
        
    }
    outfile.close
    return 0;
}