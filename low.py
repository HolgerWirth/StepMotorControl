import stepcontrol

stepcontrol.Init()

# Volle Umdrehung    
for i in range (300):    
    stepcontrol.Step8()
    stepcontrol.Step7()
    stepcontrol.Step6()
    stepcontrol.Step6()
    stepcontrol.Step4()
    stepcontrol.Step3()
    stepcontrol.Step2()
    stepcontrol.Step1()  

stepcontrol.Clean()


