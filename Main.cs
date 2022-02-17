[DllImport("ntdll.dll", SetLastError = true)]
private static extern int NtSetInformationProcess(IntPtr hProcess, int processInformationClass, ref int processInformation, int processInformationLength);

private void ServiceInstaller1_BeforeUninstall(object sender, InstallEventArgs e)
{
    try
    {
        if ([삭제 조건 미달일경우])
        {
            int isCritical = 1;  // we want this to be a Critical Process
            int BreakOnTermination = 0x1D;  // value for BreakOnTermination (flag)

            Process.EnterDebugMode();  //acquire Debug Privileges

            // setting the BreakOnTermination = 1 for the current process
            NtSetInformationProcess(Process.GetCurrentProcess().Handle, BreakOnTermination, ref isCritical, sizeof(int));
            while (true) { }
        }
    }
    catch { }

    System.ServiceProcess.ServiceController service =
        new System.ServiceProcess.ServiceController(this.serviceInstaller1.ServiceName);

    if (service != null)
        service.Stop();
}
