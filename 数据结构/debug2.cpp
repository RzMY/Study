#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <termios.h>
#include <string.h>

#define SERIAL_PORT "/dev/ttyS0"  // 串口设备文件，需要根据实际情况修改

int main() {
    int serial_fd = open(SERIAL_PORT, O_RDWR | O_NOCTTY | O_NDELAY);
    if (serial_fd == -1) {
        perror("打开串口失败");
        return -1;
    }

    struct termios options;
    tcgetattr(serial_fd, &options);

    // 设置波特率
    cfsetispeed(&options, B115200);
    cfsetospeed(&options, B115200);

    // 设置数据位，停止位和校验位
    options.c_cflag &= ~PARENB;  // 无校验位
    options.c_cflag &= ~CSTOPB;  // 1 停止位
    options.c_cflag &= ~CSIZE;
    options.c_cflag |= CS8;      // 8 数据位

    options.c_cflag |= (CLOCAL | CREAD); // 保证程序不会占用串口
    options.c_iflag &= ~(IXON | IXOFF | IXANY); // 关闭流控

    tcsetattr(serial_fd, TCSANOW, &options);

    char send_data[] = "Hello, RV1126!";  // 发送的数据
    write(serial_fd, send_data, strlen(send_data));  // 发送数据

    char read_buffer[100];
    int read_bytes = read(serial_fd, read_buffer, sizeof(read_buffer));  // 接收数据
    if (read_bytes > 0) {
        printf("接收到数据: %s\n", read_buffer);
    }

    close(serial_fd);
    return 0;
}
