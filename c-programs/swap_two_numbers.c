#include <stdio.h>

int main(){
	int x, y, temp;

	printf("Enter the value of x and y \n");
	scanf("%d%d", &x, &y);

	printf("Before swapping\nx = %d\ny = %d\n", x, y);

	temp = x;

	x = y;

	y = temp;

	printf("After swapping\nx= %d\ny = %d\n", x, y);

	return 0;
}

// Swap function in C language

//In this method we will make a function to swap numbers. We will use call by reference.


void swap(int*, int*);  // declaration of Swap function

int main() {

	int x, y;

	printf("Enter the values of x and y \n");
	scanf("%d%d", &x, &y);

	printf("Before swapping\nx= %d\ny= %d\n", x, y);

	swap(&x, &y);

	printf("After swapping\nx= %d\ny= %d\n", x, y);

	return 0;
}

//Swap function definition

void swap(int *a, int *b) {

	int temp;

	temp = *b;
	*b = *a;
	*a = temp;
}


// Swapping of two numbers without third variable

int main() {
	int a, b;

	printf("Enter the a and b to swap\n");
	scanf("%d%d", &a, &b);

	// To understand the logic choose the variables 'a' and 'b' as '4' and '5' respectively a
	a = a + b;
	b = a - b;
	a = a - b;

	printf("swap values a= %d\nb= %d\n", a, b); 

	return 0;
}

// Swap using bitwise XOR

int main() {
	int x , y;

	printf("Enter the values of x and y\n");
	scanf("%d%d", &x, &y);

	printf("Before swapping x = %d\ny = %d\n", x, y);

	x = x ^ y;
	y = x ^ y;
	x = x ^ y;

	printf("After swapping x = %d\ny = %d\n", x, y);

	return 0;
}
