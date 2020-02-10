#include <stdio.h>



int main(){
    // int *(*array[3])(int);
    // int (*ptr)[3];
    // void (*fun(int, void(*funA)(int)))(int)
    
    enum RGB  {red=10, blue, green=10, yellow};

    enum RGB rgb;


    printf("rgb color %d\n", red);
    printf("rgb color %d\n", blue);
    printf("rgb color %d\n", green);
    printf("rgb color %d\n", yellow);


    return 0;
}   
