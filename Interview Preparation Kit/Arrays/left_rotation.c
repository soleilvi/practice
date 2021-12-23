/*
Exercise from the Interview Preparation Kit "Arrays" section.

A program for shifting array contents d units to the left, where d is
a number specified by the user. It first asks for the size of the
array and d from the user, then fills an array with numbers and shifts
them to the left. Both the original and the shifted arrays are printed
for the user to see.

By Soleil Vivero
12/22/21
*/
#include <stdio.h>
#define ROW 100

void getUserInput(int *arraySize, int *leftShift);
void fillArray(int maxSize, int arraySize, int array[]);
void printArray(int maxSize, int arraySize, int array[]);
void changeIndex(int maxSize, int arraySize, int leftShift, int array[],
                 int arrShifted[]);

int main(){
  int n, d;  // n = array size, d = how much left shift you want.
  int arr[ROW], final[ROW];
  int test1[5] = {1, 2, 3, 4, 5}, test2[5] = {6, 7, 8, 9, 10};

  getUserInput(&n, &d);
  fillArray(ROW, n, arr);
  printf("Original: ");
  printArray(ROW, n, arr);
  changeIndex(ROW, n, d, arr, final);
  printf("Shifted:  ");
  printArray(ROW, n, final);

  return 0;
}

void getUserInput(int *arraySize, int *leftShift){
  printf("Input the array size and left shift (format: # #): ");
  scanf("%d %d", arraySize, leftShift);
}

void fillArray(int maxSize, int arraySize, int array[]){
  int num = 1;
  for(int i = 0; i < arraySize && i < maxSize; i++){
    array[i] = num++;
  }
}

void printArray(int maxSize, int arraySize, int array[]){
  printf("[");
  for(int i = 0; i < arraySize && i < maxSize; i++){
    if(i == arraySize - 1 || i == maxSize - 1){
      printf("%d", array[i]);
    } else{
      printf("%d, ", array[i]);
    }
  }
  printf("]\n");
}

void changeIndex(int maxSize, int arraySize, int leftShift, int array[],
int arrShifted[]){
  if(arraySize > maxSize){
    printf("The entered array size exceeds the maximum array size. (100)\n"
            "Setting the array size to the maximum size...\n");
    arraySize = maxSize;
  }
  if(leftShift > arraySize){
    leftShift -= arraySize;
  }
  for(int i = 0; i < arraySize && i < maxSize; i++){
    if(i - leftShift >= 0){
      arrShifted[i - leftShift] = array[i];
    } else{
      arrShifted[arraySize + (i - leftShift)] = array[i];
    }
  }
}
