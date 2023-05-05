# dmm6.5-esp32
DMM6.5小台表WiFI-MicroPython固件


## 使用方法：
支持 usr-vcom等虚拟串口转tcp软件，将上位机连接到小台表
支持zdd 上位机程序通过 NI-MAX  tcp 直连 小台表

## 硬件要求
支持esp32，esp32-s3 等芯片

## 硬件安装方法：
  1. 将ESP32模块的 GPIO 16，17 连接到 小台表预留的蓝牙RX，TX接口
  2. 将预留的蓝牙电源接口连接到ESP32的v3.3口
  3. 拆掉小台表的串口隔离模块
  4. 将ESP32模块的固件更新口 UART0 连接到CH340芯片的RX和TX
  5. 连接好地线
  
## 软件安装
  1. ESP32刷microPython最新版固件
  2. 使用thonny程序，将 tcp2ttl.py 上传到ESP32
  3. 修改tcp2ttl.py文件，配置SSID和PASSWORD参数，连接wifi热点
  3. 将tcp2ttl.py文件名称改成 boot.py加电自动启动
  
