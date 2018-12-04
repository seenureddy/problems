#include <stdio.h>

/*
The key process in quickSort is partition(). Target of partitions is,
given an array and an element x of array as pivot, put x at its correct 
position in sorted array and put all smaller elements (smaller than x) before x, 
and put all greater elements (greater than x) after x. 
All this should be done in linear time.
*/


void swap(int *a, int *b){
	int temp = *a;
	*a = *b;
	*b = temp;
}


int parttion(int arr[], int low, int high) {
	/* This function takes last element as pivot, places
   	   the pivot element at its correct position in sorted
       array, and places all smaller (smaller than pivot)
       to left of pivot and all greater elements to right
       of pivot 
    */

    int pivot = arr[high];

    int i = (low - 1);  // Index of smaller element

    for(int j = low; j<= high - 1; j ++) {

    	// Current element is smaller then or equal to pivot

    	if(arr[j] <= pivot){
    		i ++;
    		swap(&arr[i], &arr[j]);
    	}
    }

    swap(&arr[i + 1], &arr[high]);
    return (i + 1);
}


void quickSort(int arr[], int low, int high){

	if (low < high) {

		/* pi is partitioning index, arr[p] is now
           at right place */

		int pi = parttion(arr, low, high);

		quickSort(arr, low, pi - 1);  // Before PI
		quickSort(arr, pi + 1, high); // After PI
	}

}


void printArray(int arr[], int size){
	for(int i = 0; i < size; i++)
		printf("%d\n", arr[i]);
	printf("\n");

}


int main(){

	int arr[] = {10, 7, 8, 9, 1, 5};
	int n = sizeof(arr)/sizeof(arr[0]); // compute the size of its operand
	printf("\nx= %d\n", n);
	quickSort(arr, 0, n - 1);

	printf("Sorted array: \n");
	printArray(arr, n);
	return 0;
}
