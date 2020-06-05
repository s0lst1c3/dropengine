public class {{ special['class_name'] }}
{

    public static string {{ func_name }}()
    {
        ManagementObjectSearcher {{ v['searcher'] }} = new ManagementObjectSearcher("SELECT * FROM Win32_DiskDrive");

        foreach(ManagementObject {{ v['wmi_HD'] }} in {{ v['searcher'] }}.Get())
        {
            return {{ v['wmi_HD'] }}["SerialNumber"].ToString().Trim();
        }
        return "";

    }
}

