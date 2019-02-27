#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void
__usage()
{
    printf("--help ...");
    return;
}

int
main(char argc, char *argv[])
{
    if (argc < 2) {
        ERR("Input error");
        __usage();
        goto cleanup;
    }

    return 0;
cleanup:
    return -1;
}
