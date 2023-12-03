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
    asm volatile (".rept 461; nop; .endr");
}

void win()
{
    static char flag[256];
    static int flag_fd;
    static int flag_length;

    printf("You win! Here is your flag:\n");

    flag_fd = open("/flags/exercise2/flag", 0);

    if (flag_fd < 0)
    {
        printf("\n  ERROR: Failed to open the flag -- %s!\n", strerror(errno));
        if (geteuid() != 0)
        {
            printf("  Your effective user id is not the expected one!\n");
            printf("  You must directly run the suid binary in order to have the correct permissions!\n");
        }
        return;
    }
    flag_length = read(flag_fd, flag, sizeof(flag));
    if (flag_length <= 0)
    {
        printf("\n  ERROR: Failed to read the flag -- %s!\n", strerror(errno));
        return;
    }
    write(1, flag, flag_length);
    printf("\n\n");
}

int challenge(int argc, char **argv, char **envp)
{
    struct
    {
        char input[26];
    } data  = {0} ;
    char *input = &data.input;

    int size = 0;

    printf("Payload size: ");
    scanf("%i", &size);

    if (size > 26)
    {
        puts("Provided size is too large!");
        exit(1);
    }

    printf("Send your payload (up to %i bytes)!\n", size);
    int received = read(0, input, (unsigned int) size);

    if (received < 0)
    {
        printf("ERROR: Failed to read input -- %s!\n", strerror(errno));
        exit(1);
    }

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