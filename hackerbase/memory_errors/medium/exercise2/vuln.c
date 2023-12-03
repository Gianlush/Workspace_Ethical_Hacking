#define _GNU_SOURCE 1

#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>
#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>
#include <string.h>
#include <time.h>
#include <errno.h>
#include <assert.h>
#include <libgen.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <sys/socket.h>
#include <sys/wait.h>
#include <sys/signal.h>
#include <sys/mman.h>
#include <sys/ioctl.h>
#include <sys/sendfile.h>
#include <sys/prctl.h>
#include <sys/personality.h>
#include <arpa/inet.h>

void bin_padding()
{
    asm volatile (".rept 3293; nop; .endr");
}

int challenge(int argc, char **argv, char **envp)
{
    struct
    {
        char input[49];
        char flag[256];
    } data  = {0} ;
    char *input = &data.input;
    char *flag = &data.flag;

    unsigned long size = 0;

    read(open("/flags/exercise2/flag", 0), flag, 256);

    printf("Payload size: ");
    scanf("%lu", &size);

    printf("Send your payload (up to %lu bytes)!\n", size);
    int received = read(0, input, (unsigned long) size);

    if (received < 0)
    {
        printf("ERROR: Failed to read input -- %s!\n", strerror(errno));
        exit(1);
    }

    printf("You said: %s\n", input);

    puts("Goodbye!");

    return 0;
}

int main(int argc, char **argv, char **envp)
{
    // assert(argc > 0);

    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);

    printf("###\n");
    printf("### Welcome to %s!\n", argv[0]);
    printf("###\n");
    printf("\n");

    char crash_resistance[0x1000];

    challenge(argc, argv, envp);

    printf("### Goodbye!\n");
}