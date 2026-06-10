#include <stdio.h>
#include <pthread.h>

#define INCREMENTS 1000000

int counter = 0;

void* increment_counter(void* arg) {

    for (int i = 0; i < INCREMENTS; i++) {
        counter++;
    }

    return NULL;
}

int main() {

    pthread_t t1, t2;

    printf("Starting threads without mutex...\n");

    pthread_create(&t1, NULL, increment_counter, NULL);
    pthread_create(&t2, NULL, increment_counter, NULL);

    pthread_join(t1, NULL);
    pthread_join(t2, NULL);

    printf("Expected Counter Value: %d\n", 2 * INCREMENTS);
    printf("Final Counter Value   : %d\n", counter);

    return 0;
}