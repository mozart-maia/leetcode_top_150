#include <stdio.h>
#include <stdlib.h>


int main(){
    int casos = 0;
    int habitantes;

    scanf("%d", &casos);
    for(int i=0; i<casos; ++i){
        scanf("%d", &habitantes);
        int *arr_h;
        arr_h = (int *)malloc(habitantes * sizeof(int));
        if (arr_h == NULL){
            return -1;
        }
        for(int j=0; j<habitantes;++j){
            int h;
            scanf("%d", &h);
            arr_h[j] = h;
        }
        printf("\nPrinting array readed: ");
        for(int j=0; j<habitantes;++j){
            printf("%d ", arr_h[j]);
            
        }
        printf("\n");
    }

    return 0;
}