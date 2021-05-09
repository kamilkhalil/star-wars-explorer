function change(id)
{
    var elem = document.getElementById(id);
    if (elem.value=="unpressed") elem.value = "pressed";
    else elem.value = "unpressed";
}