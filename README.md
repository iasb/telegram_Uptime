Linux Uptime report to Telegram

1) create telegram BOT
2) record chat ID

   chat_id = 1234567890
4) record BOT ID

   bot = telepot.Bot('7123456789:AAbbccddee-aaBU3sdfghjkkln-asdfghj')
6) create file up_time.py
7) install:

   pip

   telepot
   
   telegram 
9) test up_time.py
10) create /lib/systemd/system/up_time.service

    [Unit]
      
     Description=My Lovely Service
   
    After=network.target auditd.service

    
     [Service]
    
     Type=idle
    
     Restart=on-failure
    
     User=root
    
     ExecStart=/usr/bin/python /home/user/q.py >/dev/null 2>&1  &

    
     [Install]
    
     WantedBy=multi-user.target

12) enable service

    systemctl daemon-reload

    systemctl enable up_time.service

    systemctl status up_time.service
    

14) reboot host or restart service

    
