# coding: utf-8 
# textwrap 主要为了格式化段落
import textwrap
sample_text = """
The textwrap module can be used to format
text for output in situations where prettyprinting
is desired. It offers programmatic
functionality similar to the paragraph wrapping
or filling features found in many text editors.
"""
print(textwrap.fill(sample_text,width=160))
# fill 函数会进行缩进
# 如果要移除缩进
# dedent
print(textwrap.fill(textwrap.dedent(sample_text).strip(),width=50))