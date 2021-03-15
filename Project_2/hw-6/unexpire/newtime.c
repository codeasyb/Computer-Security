// Name: Amir Ayoub
// netID: aa2078
// RUID: 198005926

#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <dlfcn.h>
#include<stdbool.h>  


time_t time(time_t *tLoc){
	
	printf("Our version time\n");
	struct tm t;
	static bool flag = false;
	time_t timeOfDay, changedTIme;
	time_t (*originalTime)(time_t *tLoc);
	originalTime = dlsym(RTLD_NEXT, "time");
	timeOfDay = (*originalTime)(tLoc);

	if(!flag && (timeOfDay < 1572546600 || timeOfDay > 1580581799)){
		t.tm_year = 2020 - 1900;  
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
// time_t time(time_t *tloc)
// {
//     printf("Entered in our version of time\n");
//     struct tm t;
//     time_t t_of_day,adjusted_time;
//      static bool flag = false;        
//     time_t (*original_time)(time_t *tloc1);
//     original_time = dlsym(RTLD_NEXT, "time");
//      t_of_day = (*original_time)(tloc);


//     if (!flag && (t_of_day < 1572546600 || t_of_day > 1580581799))
//     {
//     printf("ENTERED\n");
//     t.tm_year = 2019-1900;  // Year - 1900
//     t.tm_mon = 10;           // Month, where 0 = jan
//     t.tm_mday = 2;          // Day of the month
//     t.tm_hour = 00;
//     t.tm_min = 0;
//     t.tm_sec = 0;
//     t.tm_isdst = 0;        // Is DST on? 1 = yes, 0 = no, -1 = unknown
//     adjusted_time = mktime(&t);
//     flag = true;
//     return(adjusted_time);

//     }        
//     else
//     {
//         printf("time Function called second time\n");
//         return t_of_day;
//     }
    



// }
