import codecs
from lxml import etree


def load_xml():
    filename = '/share/region5-legends.xml'
    xml_ = codecs.open(filename, errors='ignore', encoding='utf-8')
    root = etree.parse(xml_)

    return root


def unique_tag_text(root, path):
    """'//sites/site/type'"""

    return set([elem.text for elem in root.xpath(path)])


def tag_text_max_length(root, path):
    return max(len(text) for text in unique_tag_text(root, path))


def tag_count(root, path, tag, i):
    count_xpath = (
        "{path}[count({tag})={i}]"
        .format(path=path, tag=tag, i=i)
    )

    return len([elem.tag for elem in root.xpath(count_xpath)])


def tag_counts(root, path, tag):
    return [tag_count(root, path, tag, i) for i in range(10)]


def tags(root, path):
    return set([elem.tag for elem in root.xpath(path + "/*")])


def line(root, path, tag, depth):
    xpath = "count(//{path}/{tag})".format(path=path, tag=tag)
    num = int(root.xpath(xpath))
    tcs = str(tag_counts(root, path, tag)) if num > 1 else ""
    print "{ws}{tag} {num} {tcs}".format(ws=depth * "  ", tag=tag, num=num, tcs=tcs)


def print_tags(root):
    output = []

    def loop(path=".", depth=0):
        for tag in tags(root, path):
            output.append(line(root, path, tag, depth))
            loop("{path}/{tag}".format(path=path, tag=tag), depth+1)

    loop()
    return output


if __name__ == "__main__":
    print_tags(load_xml())
