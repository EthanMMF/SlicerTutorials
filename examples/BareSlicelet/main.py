import qt
import __main__

def initSlicer(layoutWidget):
  layoutWidget.setMRMLScene(slicer.mrmlScene)
  layoutWidget.setLayout(slicer.vtkMRMLLayoutNode.SlicerLayoutOneUp3DView)
  
########################################################
## BEGIN
######################################################## 

slicerLayoutWidget = slicer.qMRMLLayoutWidget()
initSlicer(slicerLayoutWidget)

# Layout
mainWidget  = qt.QWidget()
vlayout     = qt.QVBoxLayout()
mainWidget.setLayout(vlayout)
vlayout.addWidget(slicerLayoutWidget)

# Show
mainWidget.show()
__main__.mainWidget = mainWidget # Keep track of the widget to avoid its premature destruction
