Linux Uptime report to Telegram

each 10 min in telegram will be refreshesd string:   

rpi4-18:1.18 02/07  10:27  -->   20:19

Host:IP  script_start --> last (10 min period) time

record older 10 min - deleted and new updated record inserted

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
    
     ExecStart=/usr/bin/python /home/user/q.py &

    
     [Install]
    
     WantedBy=multi-user.target

12) enable service

    systemctl daemon-reload

    systemctl enable up_time.service

    systemctl daemon-reload
    
    systemctl status up_time.service
    

14) reboot host or restart service

    systemctl start up_time.service
    
