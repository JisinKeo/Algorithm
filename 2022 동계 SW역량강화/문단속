#include <iostream>
using namespace std;
int door[2000001];
int main() {
	int N;
	cin >> N;
	for(int i=0; i<2*N; i++){
		cin >> door[i];
	}
	int temp, temp2;
	for(int i=0; i<2*N-2; i++){
		if(door[i]<0 && door[i+1]>0 && door[i+2]<0){
			temp = door[i] * -1;
			temp2 = door[i+2] * -1;
			if((temp != door[i+1]) && (temp != temp2) && (door[i+1] != temp2)){
				cout << "no";
				return 0;
			}
		}
			
	
	}	
	cout << "yes";
	return 0;
}
