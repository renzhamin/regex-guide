Regex : `^[^@ ]+@[^@.]+\.\w+$`

| String                 | Reason                                                                          | Disqualified by |
| ---------------------- | ------------------------------------------------------------------------------- | --------------- |
| `test@.com`            | After matching @ there must be 1 or more characters until "." but there is none | `[^@.]+`        |
| `test@test.gmail.com`  | After a "." is found only word characters are allowed                           | `\.\w+`         |
| `te  st@gmail.com`     | Space character not allowed                                                     | `[^@ ]+`        |
| `test@gmail@gmail.com` | After an "@" is found, there can't be any more "@" all the way to the end       | `@[^@.]+\.\w+$` |
