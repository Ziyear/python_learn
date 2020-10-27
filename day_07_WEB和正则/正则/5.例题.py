import re

source = """
<ul><li><p>
<span class="marked">runoo+b</span>，可以匹配 runoob、runooob、runoooooob 等，+ 号代表前面的字符必须至少出现一次（1次或多次）。
</p></li>
<li><p>
<span class="marked">runoo*b</span>，可以匹配 runob、runoob、runoooooob 等，* 号代表前面的字符可以不出现，也可以出现一次或者多次（0次、或1次、或多次）。
</p></li>
<li><p>
<span class="marked">colou?r</span> 可以匹配 color 或者 colour，? 问号代表前面的字符最多只可以出现一次（0次、或1次）。
</p></li></ul>
"""
sub = re.sub(r"</?\w+(\s*\w+=\"\w+\")*>", "", source)
print(sub)
