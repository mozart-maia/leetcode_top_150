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
    for(int i=0; i<9; ++i){
        int line[9] = {0};        
        for(int j=0; j<9; ++j){        
            line[j] = matrix[i][j];
  
        }
        for(int n=1; n<10; ++n){
            bool is_in_array = check_number(line, n);
            if (is_in_array == false){
                return false;
            }
        }      
    }

    for(int j=0; j<9; ++j){
        int line[9] = {0}; 
        for(int i=0; i<9; i++){
            line[i] = matrix[i][j];

        }

        for(int n=1; n<10; ++n){
            bool is_in_array = check_number(line, n);            
            if (is_in_array == false){
                return false;
            }    
        } 
    }

    int line1[9] = {matrix[0][0], matrix[0][1], matrix[0][2],matrix[1][0], matrix[1][1], matrix[1][2], matrix[2][0], matrix[2][1], matrix[2][2]};

    for(int n=1; n<10; ++n){
        bool is_in_array = check_number(line1, n);            
        if (is_in_array == false){
            return false;
        }
    } 

    int line2[9] = {matrix[0][3], matrix[0][4], matrix[0][5],matrix[1][3], matrix[1][4], matrix[1][5], matrix[2][3], matrix[2][4], matrix[2][5]};

    for(int n=1; n<10; ++n){
        bool is_in_array = check_number(line2, n);            
        if (is_in_array == false){
            return false;
        }
    } 

    int line3[9] = {matrix[0][6], matrix[0][7], matrix[0][8],matrix[1][6], matrix[1][7], matrix[1][8], matrix[2][6], matrix[2][7], matrix[2][8]};

    for(int n=1; n<10; ++n){
        bool is_in_array = check_number(line3, n);            
        if (is_in_array == false){
            return false;
        }
    } 

    int line4[9] = {matrix[3][0], matrix[3][1], matrix[3][2],matrix[4][0], matrix[4][1], matrix[4][2], matrix[5][0], matrix[5][1], matrix[5][2]};


    for(int n=1; n<10; ++n){
        bool is_in_array = check_number(line4, n);            
        if (is_in_array == false){
            return false;
        }
    } 

    int line5[9] = {matrix[3][3], matrix[3][4], matrix[3][5],matrix[4][3], matrix[4][4], matrix[4][5], matrix[5][3], matrix[5][4], matrix[5][5]};


    for(int n=1; n<10; ++n){
        bool is_in_array = check_number(line5, n);            
        if (is_in_array == false){
            return false;
        }
    } 

    int line6[9] = {matrix[3][6], matrix[3][7], matrix[3][8],matrix[4][6], matrix[4][7], matrix[4][8], matrix[5][6], matrix[5][7], matrix[5][8]};


    for(int n=1; n<10; ++n){
        bool is_in_array = check_number(line6, n);            
        if (is_in_array == false){
            return false;
        }
    } 

    int line7[9] = {matrix[6][0], matrix[6][1], matrix[6][2],matrix[7][0], matrix[7][1], matrix[7][2], matrix[8][0], matrix[8][1], matrix[8][2]};

    for(int n=1; n<10; ++n){
        bool is_in_array = check_number(line7, n);            
        if (is_in_array == false){
            return false;
        }
    } 

    int line8[9] = {matrix[6][3], matrix[6][4], matrix[6][5],matrix[7][3], matrix[7][4], matrix[7][5], matrix[8][3], matrix[8][4], matrix[8][5]};


    for(int n=1; n<10; ++n){
        bool is_in_array = check_number(line8, n);            
        if (is_in_array == false){
            return false;
        }
    } 

    int line9[9] = {matrix[6][6], matrix[6][7], matrix[6][8],matrix[7][6], matrix[7][7], matrix[7][8], matrix[8][6], matrix[8][7], matrix[8][8]};

    for(int n=1; n<10; ++n){
        bool is_in_array = check_number(line9, n);            
        if (is_in_array == false){
            return false;
        }
    } 
    
    return flag;
}

int main(){
    int jogos = 0;
    
    int matrix[9][9]; 

    scanf("%d", &jogos);
    // printf("\njogos %d\n", jogos);
    for(int n=0; n<jogos; ++n){
        printf("Instancia %d\n", n+1);
        for(int i=0; i<9; ++i){
            for(int j=0; j<9; ++j){
                int entry;
                scanf("%d", &entry);
                // printf("Instancia %d\n", entry+1);
                matrix[i][j] = entry;
            }
        }

        bool result_check_sudoku = check_sudoku(matrix);
        if (result_check_sudoku == false){
            printf("NAO\n");
        } else {
            printf("SIM\n");
        }
        printf("\n");
    
    }

    // bool result = check_sudoku(matrix);
    // printf("\nresult %d\n", result);

    return 0;
}