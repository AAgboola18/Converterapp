import PySimpleGUI as sg


ftinch_label = sg.Text("enter ft and inch:  ")
ftinch_input_box = sg.InputText(key ="ftinch")


m_label = sg.Text("Value in metres : ")
m_input_box = sg.InputText(key = "metres")

converter_btn = sg.Button("Convert")


window = sg.Window(title="Feet and inches to metres converter.")
