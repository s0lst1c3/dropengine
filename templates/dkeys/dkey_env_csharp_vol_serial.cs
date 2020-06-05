public class {{ special['class_name'] }}
{

    public static string {{ func_name }}()
    {
        ManagementObjectSearcher {{ v['searcher'] }} = new ManagementObjectSearcher("SELECT * FROM Win32_LogicalDisk");

        foreach(ManagementObject {{ v['wmi_HD'] }} in {{ v['searcher'] }}.Get())
        {
            return {{ v['wmi_HD'] }}["VolumeSerialNumber"].ToString().Insert(4, "-").Trim();
        }
        return "";

    }
}

