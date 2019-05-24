#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__="Yannick BADIE"
__date__ ="$19 Septembre 2018$"
__version__ = "$Revision: 1.1$"
__name__ = "Fan YAML Export to Markdown"

# Standard Library
from tkinter import filedialog, Tk
from os import path
from pathlib import Path

# External Library
from yaml import load, FullLoader

# Personal Library
from writemd import return_md_list, return_md_table_header, return_md_title1, return_md_title2, return_md_image

global filein
global fileout


root = Tk()
root.filename =  filedialog.askopenfilename(title = "Select file",filetypes = (("YAML files","*.yaml"),("all files","*.*")))
# TODO: if no file or cancel ==> stop program properly
filein = root.filename
directory = path.split(filein)[0]
fileout = path.splitext(filein)[0] + ".md"

# filein = "70778A020001.yaml"
# fileout = "7070778A020001.md"

with open(filein, "r") as stream:
    data = load(stream, Loader=FullLoader)
    filewrite = open(fileout, "w")

    #TITLE
    if data["Equipment"]["Amendment LTS"] != None:
        filewrite.write(return_md_title1(data["Equipment"]["P/N LTS"] + " Amdt " + data["Equipment"]["Amendment LTS"]))
    else:
        filewrite.write(return_md_title1(data["Equipment"]["P/N LTS"]))

    #IDENTIFICATION
    filewrite.write(return_md_title2("Identification"))
    for k, v in data["Equipment"].items():
        if k == "Image" or k == "3D" or k == "Performance":
            filewrite.write(return_md_list(k, return_md_image(data["Equipment"]["P/N LTS"], v)))
        else:
            filewrite.write(return_md_list(k, v))
    filewrite.write("\n")

    #POWER
    filewrite.write(return_md_title2("Power"))
    for k, v in data["Power"].items():
        filewrite.write(return_md_list(k, v))
    filewrite.write("\n")

    #CHARACTERISTICS
    filewrite.write(return_md_title2("Fan Characteristics"))
    for k, v in data["Characteristics"].items():
        filewrite.write(return_md_list(k, v))
    filewrite.write("\n")

    #DOCUMENTS
    filewrite.write(return_md_title2("Documents"))
    header = return_md_table_header({"Type": "centered", "Reference": "centered", "Title": "centered", "Issue": "centered", "LIDA Link": "centered"})
    filewrite.write(header[0])
    filewrite.write(header[1])
    for doc in data["Documents"]:
        line = ""
        for k, v in doc.items():
            line = line + "| " + str(v)
        line = line + " |\n"
        filewrite.write(line)
    filewrite.write("\n")

    #QUALIFICATION
    filewrite.write(return_md_title2("Qualification"))
    header = return_md_table_header({"Requirement": "centered", "Req #": "centered", "Standard": "centered", "Level": "centered", "Method": "centered", "SOF": "centered", "Compliant?": "centered", "Deviation": "centered"})
    filewrite.write(header[0])
    filewrite.write(header[1])
    for doc in data["Qualification"]:
        line = ""
        for k, v in doc.items():
            line = line + "| " + str(v)
        line = line + " |\n"
        filewrite.write(line)
    filewrite.write("\n")
    
    #NOISE
    filewrite.write(return_md_title2("Noise"))
    header = return_md_table_header(
        {"Octave": "centered", "Inlet": "centered", "Outlet": "centered", "Radiated": "centered"})
    for noiserecords in data["Noise"]["Noise Records"]:
        filewrite.write("### Speed : " + str(noiserecords["Speed"]) + "\n\n")
        filewrite.write("Data are in " + str(noiserecords["Noise Type"]) + " - " + str(noiserecords["Noise Unit"]) + "\n\n")
        filewrite.write(header[0])
        filewrite.write(header[1])
        for k,v in noiserecords["Octave"].items():
            string = "| " + str(k)
            for i in v:
                string = string + " | " + str(i)
            filewrite.write(string + " |\n")
        filewrite.write("\n")

    #PERFORMANCE
    filewrite.write(return_md_title2("Performance"))
    header = return_md_table_header(
        {"Airflow (L/s)": "centered", "DP (mbar)": "centered", "Power (W)": "centered", "Cosphi": "centered"})
    for perforrecord in data["Performance"]["Performance Records"]:
        filewrite.write("### Speed : " + str(perforrecord["Speed"]) + "\n\n")
        filewrite.write(header[0])
        filewrite.write(header[1])
        for performances in perforrecord["Data"]:
            string = ""
            for performance in performances:
                string = string + "| " + str(performance) + " "
            filewrite.write((string + "|\n"))
        filewrite.write("\n")

# TODO: afficher un message lorsque la conversion est réussie