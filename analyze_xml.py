import codecs
from lxml import etree


def load_xml():
    filename = '/share/region5-legends.xml'
    xml_ = codecs.open(filename, errors='ignore', encoding='utf-8')
    root = etree.parse(xml_)

    return root


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
    num = int(root.xpath("count(//" + path + "/" + tag + ")"))
    tc = str(tag_counts(root, path, tag)) if num > 1 else ""
    print "{}{} {} {}".format(depth * "  ", tag, num, tc)


def print_tags(root, path=".", depth=0):
    output = []

    def loop(path, depth):
        for tag in tags(root, path):
            output.append(line(root, path, tag, depth))
            depth += 1
            loop(path + "/" + tag, depth)
            depth -= 1

    loop(path, depth)
    return output


if __name__ == "__main__":
    print_tags(load_xml())
