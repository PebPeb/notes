
# Sockets

Documentation on [sockets](https://man7.org/linux/man-pages/man2/socket.2.html)

[`socket(...)`](https://man7.org/linux/man-pages/man2/socket.2.html) is used to create an endpoint for communication. This returns a file descriptor that refers to the endpoint.

``` C++
#include <sys/socket.h>

int socket(int domain, int type, int protocol);
```
protocol - 

## Local Communication (AF_UNIX)

The [AF_UNIX](https://man7.org/linux/man-pages/man7/unix.7.html) is a socket family specifically for establishing communication between processes on the same machine efficiently.



**Socket Address Format** - 'sun' stands for 'Socket UNIX'

``` C++
struct sockaddr_un {
  sa_family_t sun_family;
  char        sun_path[108];
}
```

*Example*

``` C++
// Creating Socket
int server_fd = socket(AF_UNIX, SOCK_STREAM, 0);

// Creating Address for AF_UNIX Socket
sockaddr_un addr{};
addr.sun_family = AF_UNIX;
strcpy(addr.sun_path, "/tmp/my_socket");

// Binding Address to Socket
bind(server_fd, (sockaddr*)&addr, sizeof(addr))
```



