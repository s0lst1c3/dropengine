public class {{ special['class_name'] }}
{
    public static string {{ func_name }}()
    {

        int {{ v['year'] }} = DateTime.Today.Year;
        int {{ v['month'] }} = DateTime.Today.Month;
        int {{ v['day'] }} = DateTime.Today.Day;

        int {{ v['g'] }}, {{ v['e'] }};
        if ({{ v['month'] }} == 1)
        {
            --{{ v['day'] }};
        }
        else if ({{ v['month'] }} == 2)
        { 
            {{ v['day'] }} += 30;
        }
        else 
        {
            {{ v['day'] }} += 28 + ({{ v['month'] }}-2)*3059/100;
            if (({{ v['year'] }} & 3) == 0)
            {
                ++{{ v['day'] }};
            }
            if (({{ v['year'] }} % 100) == 0)
            {
                --{{ v['day'] }};
            }
        }
        {{ v['g'] }} = ({{ v['year'] }}-1900)%19 + 1;
        {{ v['e'] }} = (11*{{ v['g'] }} + 18) % 30;
        if (({{ v['e'] }} == 25 && {{ v['g'] }} > 11) || {{ v['e'] }} == 24)
        {
            {{ v['e'] }}++;
        }
        switch((((({{ v['e'] }} + {{ v['day'] }})*6+11)%177)/22 & 7))
        { 

        case 0:
                return "New Moon";
        case 1:
                return "Waxing Crescent";
        case 2:
                return "First Quarter";
        case 3:
                return "Waxing Gibbous";
        case 4:
                return "Full Moon";
        case 5:
                return "Waning Gibbous";
        case 6:
                return "Third Quarter";
        default:
                return "Waning Crescent";
        }
    }
}
