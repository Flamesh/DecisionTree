from commons import functions
import pandas as pd 
moduleName = "outputs/rules/rule_0" 

tree = functions.restoreTree(moduleName)

prediction = tree.findDecision([0.000009,'udp','-','INT',2,0,104,0,111111.1072,254,0,46222220,0,0,0,0.009,0,0,0,0,0,0,0,0,0,0,52,0,2,2,1,1,2,0,0,2])


print(prediction)