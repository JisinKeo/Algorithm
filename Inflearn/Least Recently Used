// 컴퓨터구조 cache에 값을 저장하는 간단한 문제

#include <stdio.h>
#include <stdlib.h>
int main() {
	int n, m, i, j;
	int sum = 0;

	scanf("%d %d", &n, &m);

	int* cache = (int*)malloc(sizeof(int)*n);
	int* number = (int*)malloc(sizeof(int)*m);
	int cnt = 0;
	
	for(i=0; i<m; i++){
		scanf("%d", &number[i]);
	}
	for(j=0; j<n; j++){
		cache[j] = 0;
	}	
	int k = 0;
	for(i=0; i<m; i++){
		for(j=0; j<n; j++){
			if(number[i] == cache[j]){
				cnt++;
			}
		}
		
		if(cnt>0){	//hit
			for(j=n-1; j>0; j--){
				if(cache[j] == number[i]){
					k = j;
					break;
				}
			}
			for(j=k; j>0; j--){
				cache[j] = cache[j-1];
			}
			cache[0] = number[i];
		}
		
		else{
			for(j=n-1; j>0; j--){
				cache[j] = cache[j-1];
			}
			cache[0] = number[i];					
		}
		cnt = 0;
	}
	
	for(j=0; j<n; j++){
		printf("%d ", cache[j]);
	}
	free(cache);
	free(number);
		
	return 0;
}
