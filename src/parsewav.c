#include<stdio.h>
#include<malloc.h>
#include<unistd.h>
#include<string.h>
#include "header.h"

//struct HEADER *header;
int main(){
    int i, j, t = 1;
    char *sounds[] = {"samples/alienbirdcry.wav", "samples/tincan.wav", "samples/drumspiano.wav"};
    FILE * audio;
    if(audio != NULL){ 
        char *byte;
        for(i=0; i < 3; i++){
            printf("Now reading: %s\n", sounds[i]);
            audio = fopen(sounds[i],"r");
            byte = (char*) audio;
            for(j=0; j < 100; j++){
                printf("%d, ", *(byte + j));
            }
            printf("\n");
            fclose(audio);
        }
        printf("Program finished\n");
    }
    else{
        printf("Could not read the .wav file");
    }
    return 0;
}
