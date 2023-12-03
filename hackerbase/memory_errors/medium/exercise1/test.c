#include <stdio.h>
#include <string.h>
int main(){
	//char input[10] = "ciao\x00vai";
	read(0, input, 8);
	char input2[20];
	printf("len: %d\n", strlen(input));
	printf("%s",input);
	memcpy(input2, input, 8);
	printf("\n2°buf: %x",input2);
	printf("\n2° buf[5,6,7]: %c %c %c\n", input2[5], input2[6], input2[7]);


}
