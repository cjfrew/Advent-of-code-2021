#include <stdio.h>

int Test1() {

    FILE *fp;

    char buff[2047];

    fp = fopen("data.txt", "r");
    
    fscanf(fp, "%d",buff);
    
    for(int i = 0; i < (getc(buff) != EOF); i++ ) {
        printf(buff[i]);
    }
}

int main() { 

    Test1();

}
