public class {{ special['class_name'] }}
{
    public static void {{ func_name }}()
    {
        if (Registry.LocalMachine.OpenSubKey(@"SYSTEM\ControlSet001\Enum\USBSTOR", false).GetSubKeyNames().Length < 2)
        {
            System.Environment.Exit(0);
        }
    }
}
