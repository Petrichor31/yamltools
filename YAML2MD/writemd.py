#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__="Yannick BADIE"
__date__ ="$01 February2018$"
__version__ = "$Revision: 0.1$"
__name__ = "Fan YAML File Verification"

# Standard Library

def return_md_list(key, value):
    string = "* " + str(key) + " : " + str(value) + "  \n"
    return string

def return_md_table_header(dict):
    headertext =""
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
    header = (headertext, headerformat)
    return header

def return_md_image(alttext, imagelink):
    string = "![" + str(alttext) + "](" + str(imagelink) + ")"
    return string

def return_md_title1(title):
    titleline = "# " + str(title) + "\n\n"
    return titleline

def return_md_title2(title):
    titleline = "## " + str(title) + "  \n\n"
    return titleline
