# TornadoService HTB challenge WRITEUP
[Exploit.py](Exploit/exploit-server.py) Made by: [Gianlush](https://github.com/Gianlush/)

## step 1: analisi codice
Dal codice sorgente si nota immediatamente la classe `ProtectedContentHandler` all'interno del `main.py` che restituisce direttamente la flag per superare la challenge. Tuttavia, per potere visitare l'endpoint correlato: `/stats` è necessario essere loggati. 

Un'altro endpoint interessante è `/report_tornado` che consente di inviare un indirizzo IP il quale verrà visitato da un BOT, il che fa subito pensare ad una possibile **SSRF**. Il metodo che gestisce l'endpoint `/update_tornado` è consentito solo in **localhost**, che nell'ottica della challenge potrebbe servire a nascondere un comportamento particolare che si potrebbe testare con una **SSRF**.

## step 2: tentativo di SSRF
