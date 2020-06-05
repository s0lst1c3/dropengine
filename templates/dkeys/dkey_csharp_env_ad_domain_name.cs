public class {{ special['class_name'] }}
{

    public static string {{ func_name }}()
    {
        try
        {
            return System.DirectoryServices.ActiveDirectory.Domain.GetComputerDomain().Name;
        }
        catch
        {
            return Environment.UserDomainName;
        }
    }
}
