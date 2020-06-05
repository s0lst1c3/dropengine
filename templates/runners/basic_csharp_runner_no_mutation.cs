{{ rendered_imports }}

public class {{ class_name }}
{
    public static void {{ func_name }}()
    {
        {{ special['payload_main_class_name'] }}.{{ special['payload_main_func_name'] }}();
        return;
    }
}

{{ rendered_inner_shell }}
