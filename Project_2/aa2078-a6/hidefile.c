// Name: Amir Ayoub
// netID: aa2078
// RUID: 198005926

#define _GNU_SOURCE
#include <stdio.h>
#include <unistd.h>
#include <dlfcn.h>
#include <string.h>
#include <dirent.h>
#include <stdlib.h>

struct dirent *readdir(DIR *dir){

    struct dirent *dPointer = NULL;
    struct dirent *(*fptr)(DIR *dir);
    char *hideFile = getenv("HIDDEN");

    fptr = dlsym(RTLD_NEXT, "readdir");

    dPointer = fptr(dir);
    if(dPointer != NULL){
        if(hideFile && strcmp(dPointer->d_name, hideFile) == 0){
            dPointer = fptr(dir);
        }
        printf("file: %s\n", dPointer->d_name);
    }
    return dPointer;
}