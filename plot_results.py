#! /usr/bin/env python
print("Risultati simulazione convertitore forward")
filename = "results_forward_0000.txt" 
print("File utilizzato: " , filename)

tabular_results_file = open(filename, 'r')
tabular_lines = tabular_results_file.readlines()
tabular_lines = [line.strip() for line in tabular_lines] # toglie new line e spazi dalle righe

time = [] # <-- tempo di simulazione
switch_driver_voltage = [] # <-- Tensione del driver di uno switch
primar_inductor_voltage = [] # <-- Tensione ai capi dell'induttanza di primario
primar_inductor_current = [] # <-- Corrente entrante nell'induttanza di primario
freewheeling_diode_current = [] # <-- Corrente nel diodo di ricircolo

