#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char *data;
    size_t length;
    size_t capacity;
} StringBuffer;

StringBuffer* sb_init(size_t initial_capacity) {

    if (initial_capacity == 0) {
        initial_capacity = 1;
    }

    StringBuffer *sb = malloc(sizeof(StringBuffer));

    if (sb == NULL) {
        printf("Memory allocation failed for StringBuffer.\n");
        return NULL;
    }

    sb->data = malloc(initial_capacity);

    if (sb->data == NULL) {
        printf("Memory allocation failed for data buffer.\n");
        free(sb);
        return NULL;
    }

    sb->length = 0;
    sb->capacity = initial_capacity;
    sb->data[0] = '\0';

    return sb;
}

void sb_append(StringBuffer *sb, const char *str) {

    if (sb == NULL || str == NULL) {
        return;
    }

    size_t str_len = strlen(str);

    // Grow buffer when capacity is insufficient
    while (sb->length + str_len + 1 > sb->capacity) {

        size_t new_capacity = sb->capacity * 2;

        // Safe realloc
        char *temp = realloc(sb->data, new_capacity);

        if (temp == NULL) {
            printf("Reallocation failed.\n");
            return;
        }

        sb->data = temp;
        sb->capacity = new_capacity;

        printf("Buffer resized to capacity: %zu\n", sb->capacity);
    }

    strcpy(sb->data + sb->length, str);
    sb->length += str_len;
}

void sb_free(StringBuffer *sb) {

    if (sb != NULL) {
        free(sb->data);
        free(sb);
    }
}

int main() {

    StringBuffer *sb = sb_init(8);

    if (sb == NULL) {
        return 1;
    }

    printf("Initial Capacity: %zu\n\n", sb->capacity);

    sb_append(sb, "Hello");

    printf("String: %s\n", sb->data);
    printf("Length: %zu\n", sb->length);
    printf("Capacity: %zu\n\n", sb->capacity);

    sb_append(sb, " World!");

    printf("String: %s\n", sb->data);
    printf("Length: %zu\n", sb->length);
    printf("Capacity: %zu\n\n", sb->capacity);

    sb_append(sb, " Dynamic String Buffer Example");

    printf("String: %s\n", sb->data);
    printf("Length: %zu\n", sb->length);
    printf("Capacity: %zu\n\n", sb->capacity);

    sb_free(sb);

    printf("All memory freed successfully.\n");

    return 0;
}