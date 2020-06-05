public class {{ special['class_name'] }}
{
    public static byte[] {{ func_name }}(byte[] {{ v['ct'] }}, byte[] {{ v['ekey'] }})
    {
        byte [] {{ v['iv'] }} = {{ special['crypter_data']['iv_array'] }};
        SHA256Managed {{ v['hashstring'] }} = new SHA256Managed();
        byte[] {{ v['hashed_key'] }} = {{ v['hashstring'] }}.ComputeHash({{ v['ekey'] }});

            using (RijndaelManaged {{ v['rijAlg'] }} = new RijndaelManaged())
            {
                {{ v['rijAlg'] }}.Key = {{ v['hashed_key'] }};
                {{ v['rijAlg'] }}.IV = {{ v['iv'] }};
                {{ v['rijAlg'] }}.Padding = PaddingMode.PKCS7;
                {{ v['rijAlg'] }}.BlockSize = 128;
                {{ v['rijAlg'] }}.Mode = CipherMode.CBC;
                ICryptoTransform {{ v['decryptor'] }} = {{ v['rijAlg'] }}.CreateDecryptor({{ v['rijAlg'] }}.Key, {{ v['rijAlg'] }}.IV);

                return {{ v['decryptor'] }}.TransformFinalBlock({{ v['ct'] }}, 0, {{ v['ct'] }}.Length);
            }
    }
}
