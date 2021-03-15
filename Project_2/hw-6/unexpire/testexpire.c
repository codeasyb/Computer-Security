#include <stdio.h>
#include <time.h>

int main(void) {
    struct tm t;
    time_t t_of_day;
    t_of_day = time(NULL);
    printf("Time retunred from functions is %ld\n",t_of_day);

    if (t_of_day >= 1572546600 && t_of_day <=1580581799)
    {
        printf("PASSED! You reset the time successfully!\n")   ; 
    }
    else
    {
        printf("Your valdiation is expired\n")   ; 

    }
    printf("Calling second time time function:\n");
    t_of_day = time(NULL);
    printf("Time retunred from functions is %ld\n",t_of_day);
    
    
    


}
