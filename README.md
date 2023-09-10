# Fucking Damn 3rd party cititaion

# 他引计数脚本
功能：
1. 输入两个`.bib`文件，其中第一个仅包含一篇需要统计他引的文献，第二个文件包含所有引用了被统计文献的文献
2. 脚本统计第二个`.bib`文件中，作者群与待统计文献不存在交叉的文献条目数
3. 脚本首先输出存在自引的文献编号以及作者的交集
4. 然后输出总引用数和他引数目

# 输入文件的要求
必须包含`author`字段。

# 示例
```bash
% ./check_citation.py example/2009astro2010S..82F.bib example/2009astro2010S..82F.cit.bib
2013PhRvD..87d3005D : [Person('{Tegmark}, Max')]
2012MNRAS.419.3491L : [Person('{Tegmark}, Max')]
2011MNRAS.413.1174P : [Person('{Peterson}, Jeffrey B.')]
2011JCAP...04..038B : [Person('{Loeb}, Abraham')]
2011MNRAS.410.2075L : [Person('{Tegmark}, Max'), Person('{Zaldarriaga}, Matias')]
id: 2009astro2010S..82F
Title: {Cosmology from the Highly-Redshifted 21 cm Line}
Number of all cit: 26
Number of 3rd cit: 21
```
