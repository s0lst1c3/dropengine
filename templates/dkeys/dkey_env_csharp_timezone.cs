public class {{ special['class_name'] }}
{

    public static string {{ func_name }}()
    {
        return Convert.ToString(System.TimeZone.CurrentTimeZone.GetUtcOffset(DateTime.Now)).Substring(0,3);
    }
}
