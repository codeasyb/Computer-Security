// Name: Amir Ayoub
// netID: aa2078
// RUID: 198005926
#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <dlfcn.h>
#include <stdbool.h>  

time_t time(time_t *tLoc){
	struct tm t;
	static bool flag = false;
	time_t timeOfDay, changedTIme;
	time_t (*originalTime)(time_t *tLoc);
	originalTime = dlsym(RTLD_NEXT, "time");
	timeOfDay = (*originalTime)(tLoc);

	if(!flag && (timeOfDay < 1572546600 || timeOfDay > 1580581799)){
		t.tm_year = 2030 - 1900;  
    	t.tm_mon = 11;          
	    t.tm_mday = 30;         
    	t.tm_hour = 23;
	    t.tm_min = 0;
	    t.tm_sec = 0;
	    t.tm_isdst = 0;        
	    changedTIme = mktime(&t);
	    flag = true;
	    return changedTIme;
	}else {
		return timeOfDay;
	}
}