#include <stdio.h>
#include <stdlib.h>

int comp(const void *a, const void *b) {
    return (*(int *)a - *(int *)b);
}

int main(){
    int casos = 0;
    int habitantes;

    scanf("%d", &casos);
    for(int i=0; i<casos; ++i){
        scanf("%d", &habitantes);
        int *arr_h;
        arr_h = (int *)malloc(habitantes * sizeof(int));
        if (arr_h == NULL){
            printf("Erro no malloc!\n");
            return -1;
        }
        for(int j=0; j<habitantes;++j){
            int h;
            scanf("%d", &h);
            arr_h[j] = h;
        }

        // printf("\nPrinting array readed: ");
        // for(int j=0; j<habitantes;++j){
            // printf("%d ", arr_h[j]);            
        // }
        // printf("\n");

        qsort(arr_h, habitantes, sizeof(arr_h[0]), comp);
        
        // printf("\nPrinting array sorted: ");

        for(int j=0; j<habitantes-1;++j){
            printf("%d ", arr_h[j]);            
        }
        printf("%d\n", arr_h[habitantes-1]);
    }

    return 0;
}