Web server with the function of searching for processes in the task manager.
return 0 or 1
0 - the process is not running
1 - working process
You can use it for example with Zabbix. Zabbix sends a request to the server and gets 0 or 1 from it. You can then use the trigger to send an email to the system administrator.
