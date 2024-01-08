
import sys
import maya.cmds as cmds



dir_path=r'Z:\users\arodriguez\scripts\maya_tools'
sys.path.append(dir_path)



def colorTemperature_tool_run(*args):
    
    from colorTemperature_tool import colortemperatureTool_UI_run 
    colortemperatureTool_UI_run() 
     
    
def sample_too_run(*args):
    
    from sample_tool import samplesTool_UI_run 
    samplesTool_UI_run()           
    
    
def layerTool_run(*args):
    
    from layer_tool import layerTool_UI_run 
    layerTool_UI_run()  
    
    
   
def lightingTool_UI_run():        
    
    '''

    .......... UI .............

    '''    



    lightingeTool_window='lighting_tools'


    # checking if the window UI exists

    if cmds.window(lightingeTool_window, exists=True):
        cmds.deleteUI(lightingeTool_window)
        
    else:
        print ('THERE IS NO WINDOW')    

    # FIRST TAB
    # Setting the window variable and naming
    lightingeTool_window = cmds.window('lighting_tools')

    cmds.columnLayout()
    cmds.separator(h=10)
    cmds.text( label='LIGHTING DEPARTMENT TOOLS', width=200, align= 'center' )
    cmds.separator(h=10)

    cmds.button( label='color temperature tool', command=colorTemperature_tool_run, width = 380)
    cmds.separator(h=10)
    cmds.button( label='Arnold samples tool', command=sample_too_run, width = 380)
    cmds.separator(h=10)
    cmds.button( label='layer tool', command=layerTool_run, width = 380)


    cmds.setParent('..')



    cmds.showWindow( lightingeTool_window )





