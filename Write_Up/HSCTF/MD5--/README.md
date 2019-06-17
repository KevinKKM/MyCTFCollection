## MD5-- ##

In this question, it provided source code to us:<br><br>
<?php
$flag = file_get_contents("/flag");

if (!isset($_GET["md4"]))
{
highlight_file(__FILE__);
die();
}

if ($_GET["md4"] == hash("md4", $_GET["md4"]))
{
echo $flag;
}
else
{
echo "bad";
}
?>

<br>
As we can see, it using md4 = Hash(md4) for checking. Since it's a PHP script, we can understand that's 0e php hash vulnerability.
<br><br>
However, since this script using MD4 instead of MD5, it's very diffcult to find the exist vulnerability result to get the flag. So we have to use our program to obtain the vulnerability output.
<br><br>
After the Python Script(around 5-6 hour....),we can get 0e251288019, after MD4 hash become: 0e874956163641961271069404332409.
<br><br>
In PHP, if we cast the number 0e237481374, it just simply become 0, such that:
<pre>
0e251288019==MD4(0e251288019)
->0e251288019==0e874956163641961271069404332409
->0==0
->True
</pre> 
By this result, we can bypass the authentication and get the flag
<br>
FLAG:hsctf{php_type_juggling_is_fun}

