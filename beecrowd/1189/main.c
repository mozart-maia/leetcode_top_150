#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
    char op[2];
    double matrix[12][12];
    double soma=0, nmedia=0;

    scanf("%s", op);

    for(int i=0; i<12; ++i){
        for(int j=0; j<12; ++j){
            double input;
            scanf("%lf", &input);
            matrix[i][j] = input;
        }
    }

    int coluna = 1;
    int half = -1;

    for(int i=1; i<11; ++i){        
        for(int j=0; j< coluna; ++j){
            // printf("\nvalor: %f - coluna: %d - half: %d", matrix[i][j], coluna, half);
            soma += matrix[i][j];
            ++nmedia;
        }
        if(coluna == 5){
            half += 1;
        }
        if(half==-1){
            coluna += 1;
        }
        if(half>0){
            coluna = coluna - 1;
        }
    }

    int is_media = strcmp("S", op);
    // printf("\nis_media: %d", is_media);

    if (is_media){
        printf("%.1f\n", soma / nmedia);
    } else {
        printf("%.1f\n", soma);
    }    
    return 0;
}