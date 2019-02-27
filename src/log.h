#ifndef _LOG_H_
#define _LOG_H_

#include <stdio.h>

#define DBG(format, msg, ...) \
    fprintf(stdout, "[DBG] (%s:%d)" msg "\n", __func__, __LINE__, __VA_ARGS__);

#define INF(format, msg, ...) \
    fprintf(stdout, "[INF] (%s:%d)" msg "\n", __func__, __LINE__, __VA_ARGS__);

#define ERR(format, msg, ...) \
    fprintf(stderr, "[ERR] (%s:%d)" msg "\n", __func__, __LINE__, __VA_ARGS__);

#endif