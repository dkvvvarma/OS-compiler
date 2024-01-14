#include<stdio.h>

int main()
{
    int page_number, page_size, memory_size, offset, physical_address;
    
    printf("Enter page number: ");
    scanf("%d", &page_number);
    
    printf("Enter page size: ");
    scanf("%d", &page_size);
    
    printf("Enter memory size: ");
    scanf("%d", &memory_size);
    
    printf("Enter offset: ");
    scanf("%d", &offset);
    
    physical_address = (page_number * page_size) + offset;
    
    if(physical_address > memory_size)
    {
        printf("Error: Invalid memory access!\n");
    }
    else
    {
        printf("Physical address is: %d\n", physical_address);
    }
    
    return 0;
}