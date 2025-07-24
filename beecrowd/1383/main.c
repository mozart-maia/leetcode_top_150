#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

bool check_number(int arr[9], int n){
    for(int i=0; i<9; ++i){
        if (arr[i]==n){
            return true;
        }
    }
    return false;
}

bool check_sudoku(int matrix[9][9]){
    bool flag = true;

    int line[9] = {0};
    // TODO: Check for cols using decrement for
    // int col[9] = {0};
    for(int i=0; i<9; ++i){        
        for(int j=0; j<9; ++j){
        
            line[j] = matrix[i][j];
            printf("%d ", matrix[i][j]);
        }

        for(int n=1; n<10; ++n){
            bool is_in_array = check_number(line, n);
            if (is_in_array == false){
                return false;
            }
        }

        
        printf("\n");
        // printf("\nline result: %d\n", line);
    }

    
    return flag;
}

int main(){
    int jogos = 0;
    
    int matrix[9][9]; 

    scanf("%d", &jogos);
    printf("\njogos %d\n", jogos);
    for(int n=0; n<jogos; ++n){
        printf("\nn:  %d\n", n);
        for(int i=0; i<9; ++i){
            for(int j=0; j<9; ++j){
                int entry;
                scanf("%d", &entry);
                // printf("\nentry %d\n", entry);
                matrix[i][j] = entry;
            }
        }

        bool result_check_sudoku = check_sudoku(matrix);
        if (result_check_sudoku == false){
            printf("\nNot sudoku solution...\n");
        } else {
            printf("\nIt is a sudoku solution!\n");
        }
    
    }

    // bool result = check_sudoku(matrix);
    // printf("\nresult %d\n", result);

    return 0;
}