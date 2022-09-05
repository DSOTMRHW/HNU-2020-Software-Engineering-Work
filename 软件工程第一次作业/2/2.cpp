#include <stdio.h>

int main(){
	int n = 0;
	scanf("%d",&n);
	int a[n] = {0};
	for(int i = 0;i < n;i++){
		scanf("%d",&a[i]);
	}
	int	max = 0;
	for (int i = 0;i < n;i++) {
		int sum = 0;
		for (int j = i;j < n;j++) {
			sum = sum + a[j];
			if (sum > max) {
				max = sum;
			}
		}
	}
	printf("%d",max);
}
