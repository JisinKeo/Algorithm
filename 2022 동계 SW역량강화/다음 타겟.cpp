#include <iostream>
using namespace std;
int main() {
	long int n;
	cin >> n;
	for(long int i=0; i<n; i++){
		long int xh,yh,xn,yn,xt,yt;
		long int x = 0, y = 0;
		cin >> xh >> yh >> xn >> yn >> xt >> yt;
		
		if(xh<xn){
			y = ((yn-yh)*(xt-xh))/(xn-xh)+yh;
			if(y>yt){
				cout << "2" << "\n";
			}
			else if(y<yt){
				cout << "1" << "\n";
			}
			else{
				cout << "3" << "\n";
			}
		}
		else if(xh>xn){
			y = ((yn-yh)*(xt-xh))/(xn-xh)+yh;
			if(y>yt){
				cout << "1" << "\n";
			}
			else if(y<yt){
				cout << "2" << "\n";
			}
			else{
				cout << "3" << "\n";
			}			
		}
		else if(xh==xn){
			if(xh>xt){
				cout << "1" << "\n";
			}
			else if(xh<xt){
				cout << "2" << "\n";
			}
			else{
				cout << "3" << "\n";
			}
		}
	}
	
	return 0;
}
