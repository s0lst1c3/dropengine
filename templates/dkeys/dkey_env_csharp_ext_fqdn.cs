public class {{ special['class_name'] }}
{

    public static string {{ func_name }}()
    {
        HttpWebRequest {{ v['request'] }} = (HttpWebRequest)WebRequest.Create("{{ special['ekey_data']['source'] }}");
        {{ v['request'] }}.AutomaticDecompression = DecompressionMethods.GZip | DecompressionMethods.Deflate;
    
        using(HttpWebResponse {{ v['response'] }} = (HttpWebResponse){{ v['request'] }}.GetResponse())
        using(Stream {{ v['stream'] }} = {{ v['response'] }}.GetResponseStream())
        using(StreamReader {{ v['reader'] }} = new StreamReader({{ v['stream'] }}))
        {
            return {{ v['reader'] }}.ReadToEnd().Trim();
        }
    }
}

