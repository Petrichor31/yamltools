#!/usr/bin/python3
# coding: utf-8

__author__="Yannick BADIE"
__date__ ="$21 August 2019$"
__version__ = "$Revision: 1.0$"
__name__ = "Fan YAML File Verification"

# Standard Libraries

# External Libraries

# Personal Module


def return_md_list(key, value):
    """
        Convert two parameters in a formatted string as markdown list with return line (\\n).
        :param key: first part of the list
        :type key: can be anything, it will be converted to string
        :param value: second part of the list
        :type value: can be anything, it will be converted to string
        :return: string formatted as: "key: value  \n"
        :rtype: string

        :Example:

        >>> return_md_list("Spam", 42)
        '* Spam : 42  \\n'

    """
    string = "* " + str(key) + " : " + str(value) + "  \n"
    return string


def return_md_table_header(dict):
    """
        Convert a dictionnary {"Spam": "centered", "Bacon": "left-aligned", "Egg": "right-aligned"}
        into tuple. First item is the header titles, second item is for formmating (centered, left-aligned, right-aligned).
        Both are formatted for a markdown table.
        :param dict:
        :type dict: dictionnary
        :return:
        :rtype: list of strings

        :Example:

        >>> return_md_table_header({"Spam": "centered", "Bacon": "left-aligned", "Egg": "right-aligned"})
        ['| Spam| Bacon| Egg|\\n', '|:---:|:---|---:|\\n']
    """
    headertext = ""
    headerformat = ""
    for k, v in dict.items():
        headertext = headertext + "| " + str(k)
        if (v == "centered"):
            headerformat = headerformat + "|:---:"
        elif (v == "left-aligned"):
            headerformat = headerformat + "|:---"
        elif (v == "right-aligned"):
            headerformat = headerformat + "|---:"
    headerformat = headerformat + "|\n"
    headertext = headertext + "|\n"
    header = [headertext, headerformat]
    return header


def return_md_image(alttext, imagelink):
    """
        Convert two strings into a markdown link for an image.
        :param alttext: alternative text for the link when link is missing
        :type alttext: string
        :param imagelink: image link
        :type imagelink: string
        :return: link with markdown format
        :rtype: string

        :Example:

        >>> return_md_image("Spam Spam Spam", "https://linknow.com/wp-content/uploads/2016/03/spam-monty-python.gif")
        '![Spam Spam Spam](https://linknow.com/wp-content/uploads/2016/03/spam-monty-python.gif)'
    """
    string = "![" + str(alttext) + "](" + str(imagelink) + ")"
    return string


def return_md_title1(title):
    """
        Convert a string into a markdown Title 1 (#)
        :param title: line which will be used for the title
        :type title: string
        :return: return a line formatted as a markdown title 1
        :rtype: string

        :Example:

        >>> return_md_title1("SPAM1")
        '# SPAM1\\n\\n'
    """
    title_line = "# " + str(title) + "\n\n"
    return title_line


def return_md_title2(title):
    """
        Convert a string into a markdown Title 2 (##)
        :param title: line which will be used for the title
        :type title: string
        :return: return a line formatted as a markdown title 2
        :rtype: string

        :Example:

        >>> return_md_title2("SPAM2")
        '## SPAM2  \\n\\n'
    """
    titleline = "## " + str(title) + "  \n\n"
    return titleline


if __name__ == "Fan YAML File Verification":
    import doctest
    doctest.testmod()