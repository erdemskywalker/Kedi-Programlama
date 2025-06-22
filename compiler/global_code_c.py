global_code_one="""

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>







typedef struct 
{
    char *veri;
    int boyut;
    int kapasite;
} kedi_default_typedef_string;


kedi_default_typedef_string kedi_default_add_typedef_string(const char *first){
    int len = strlen(first);
    int kapasite = len + 1;
    kedi_default_typedef_string d;
    d.boyut = len;
    d.kapasite = kapasite;
    d.veri = malloc(kapasite);
    strcpy(d.veri, first);
    return d;
}

void kedi_default_assignment_typedef_string(kedi_default_typedef_string *d, const char *new_data){
    int len=strlen(new_data);
    if(len+1>d->kapasite){
        d->kapasite=len+1;
        d->veri = realloc(d->veri,d->kapasite);
    }
    strcpy(d->veri,new_data);
    d->boyut=len;
}


int yazı_karşılaştır(const char *str1, const char *str2) {
    while (*str1 && *str2) {
        if (*str1 != *str2) {
            return 0;  
        }
        str1++;
        str2++;
    } 
    return (*str1 == '\\0' && *str2 == '\\0');
}

"""
