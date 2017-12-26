#include <stdio.h>
#include <stdint.h>
int main()
{
 int32_t a = 1;
 int32_t b = 109900;
 int32_t c = 126900;
 int32_t d = 2;
 int32_t e = 2;
 int32_t f = 1;
 int32_t g = 0;
 int32_t h = 0;
 int32_t p = 0;
 while(1)
 {
    f = 1;
    d = 2;
    while(1)
    {
        e = 2;
        while(1)
        {
            g = d;
            g *= e;
            g -= b;
            if (g == 0)
            {
                f = 0;
            }
            e -= 1;
            g = e;
            g -= b;
            if (g == 0)
            {
                break;
            }
        }
        d -= 1;
        g = d;
        g -= b;
        if (g == 0)
        {
            break;
        }
        if (f == 0)
        {
            h -= -1;
        }
        g = b;
        g -= c;
        if (g == 0)
        {
            printf("h = %d\n", h);
            printf("Exiting program!\n");
            return 0;
        }
        b -= 17;
    }
 }
}