import stepcontrol

stepcontrol.Init()

# Volle Umdrehung    
for i in range (300):
    stepcontrol.Step1()
    stepcontrol.Step2()
    stepcontrol.Step3()
    stepcontrol.Step4()
    stepcontrol.Step5()
    stepcontrol.Step6()
    stepcontrol.Step7()
    stepcontrol.Step8()  

stepcontrol.Clean()

