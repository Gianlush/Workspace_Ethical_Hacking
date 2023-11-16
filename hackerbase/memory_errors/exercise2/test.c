#include <assert.h>
#include <stdio.h>
#include <limits.h>

int main(){

	printf("unint max: %u\n", UINT_MAX);
	unsigned long long size = 0;

	unsigned int record_num;
	unsigned int record_size;
	printf("Number of payload records to send: ");
	scanf("%u", &record_num);
	assert(record_num > 0);
	printf("Size of each payload record: ");
	scanf("%u", &record_size);
	assert(record_size > 0);
	size = record_num;
	size *= record_size;
	printf("size llu: %llu\n", size);
	printf("size lu: %lu\n", size);
	printf("num*size in uint: %u\n", record_size * record_num);
	assert(record_size * record_num <= 86);
}
