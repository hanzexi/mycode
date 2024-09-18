name = "  这 是 一 个 不带 空 格 的 句 子。  "
print(name.split())

name1 = "\t这\t是\t一\t个\t带\t制\t表\t符\t的\t句\t子。\t"#制表符

name2 = "\n这\n是\n一\n个\n带\n换\n行\n符\n的\n句\n子。\n"#换行符

name = "\n\t这\n\t是\n\t一\n\t个\n\t带\n\t空\n\t格\n\t的\n\t句\n\t子。\n\t"#换行符+制表符
print(name,name1,name2)