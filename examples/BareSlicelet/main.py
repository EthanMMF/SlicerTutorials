import qt
import __main__

def initSlicer(layoutManager, layoutWidget):
  layoutManager.setMRMLScene(slicer.mrmlScene) 
  layoutManager.setScriptedDisplayableManagerDirectory(slicer.app.slicerHome + "/bin/Python/mrmlDisplayableManager") 
  layoutWidget.setLayoutManager(layoutManager) 
  slicer.app.setLayoutManager(layoutManager) 
  layoutWidget.setLayout(slicer.vtkMRMLLayoutNode.SlicerLayoutFourUpView) 
  return layoutWidget
  
########################################################
## BEGIN
######################################################## 

mainWidget    = qt.QWidget()
layoutWidget  = initSlicer(slicer.qSlicerLayoutManager(), slicer.qMRMLLayoutWidget())

# Layout
vlayout     = qt.QVBoxLayout()
mainWidget.setLayout(vlayout)
vlayout.addWidget(layoutWidget)

# Show
mainWidget.show()
__main__.mainWidget = mainWidget # Keep track of the widget to avoid its premature destruction