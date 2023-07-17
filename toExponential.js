inlets  = 1;
outlets = 2;

function dictionary(d_name)
{
    var dict = new Dict(d_name);

    var min = dict.get("min");
    var max = dict.get("max");

    if(min != "")
    {
        min = min.toExponential();
    }

    if(max != "")
    {
        max = max.toExponential();
    }

    outlet(1, max);
    outlet(0, min);
}