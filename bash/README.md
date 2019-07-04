## Search on up file times
> Access time (-atime): This is the last timestamp of when the file was accessed by some user
> Modification time (-mtime): This is the last timestamp of when the file content was modified
> Change time (-ctime): This the last timestamp of when the metadata for a file (such as permissions or ownership) was modified
##下面fork()用于创建子进程
对于被创建的紫禁城，fork()将返回0值，对于原进程则返回紫禁城的进程号PID。
该子进程关闭了句柄0,以只读方式打开/etc/rc文件，并使用execve()函数将进程自身替换成/bin/sh程序，然后执行，所携带的参数和环境变量分别由argv_rc和envp_rc数组给出。关闭句柄0并立刻打开/etc/rc文件的作用是吧标准输入stdin重定向到/etc/rc文件。这样shell程序/bin/sh就可以运行rc文件中设置的命令
'''
if (!(pid=fork())){
    close(0);
    if (open("/etc/rc", O_RDONLY,0))
        exit(1);
    execve("/bin/sh", argv_rc, envp_rc);
    _exit(2);
}
'''
下面作用是父进程等待子进程的结束，&i是存放返回状态信息的位置。
'''
if (pid>0)
    while(pid != wait(&i))
        /* nothing */

'''
关闭所有以前还遗留的句柄，新创建一个绘画并设置进程组号，然后重新打开/dev/tty0作为stdin,并复制成stdout和stderr.再次执行系统解释程序/bin/sh.
'''
while(1){
    if ((pid=fork())<0){
        printf("Fork failed in init\r\n");
        continue;
    }
    if(!pid){
        close(0);close(1);close(2);
        setsid();
        (void) open("/dev/tty0", 0_RDWR,0);
        (void) dup(0);
        (void) dup(0);
        _exit(execve("/bin/sh",argv,envp));
    }
    while(1)
        if(pid == wait(&i))
            break;
    printf("\n\rchild %d died with code %04x\n\r",pid,i);
    sync();
}
_exit(0);
'''

#字符设备驱动程序（char driver）

