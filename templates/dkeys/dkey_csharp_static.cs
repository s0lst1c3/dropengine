public class {{ special['class_name'] }}
{
    public static string {{ func_name }}()
    {
        byte[] {{ v['dkey'] }} = {{ special['ekey_data']['val_array'] }};

        return Encoding.UTF8.GetString({{ v['dkey'] }});
    }
}
