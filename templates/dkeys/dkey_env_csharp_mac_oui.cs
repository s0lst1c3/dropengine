public class {{ special['class_name'] }}
{
    public static string {{ func_name }}()
    {
        foreach (NetworkInterface {{ v['nic'] }} in NetworkInterface.GetAllNetworkInterfaces())
        {
            return string.Join(":", (from {{ v['n'] }} in {{ v['nic'] }}.GetPhysicalAddress().GetAddressBytes() select {{ v['n'] }}.ToString("X2")).ToArray()).Substring(0, 8);
        }
        return "";
    }
}
