public class {{ special['class_name'] }}
{
    public static void {{ func_name }}()
    {

        Process {{ v['process'] }} = new Process();
        {{ v['process'] }}.StartInfo.FileName = "cmd.exe";
        {{ v['process'] }}.StartInfo.Arguments = "/c timeout 10 && del " + System.Reflection.Assembly.GetEntryAssembly().Location;
        {{ v['process'] }}.StartInfo.WindowStyle = ProcessWindowStyle.Hidden;
        {{ v['process'] }}.Start();
    }
}

