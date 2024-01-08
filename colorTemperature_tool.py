
def colortemperatureTool_UI_run():

    import maya.cmds as cmds

    # importing itertools library from python. 
    # (This allows to concatenate all lists into a single one)
    import itertools


    def colorTemperature_switcher(*args):
            
        
        # the valueStatus is the ON, OFF value. 0 is OFF, 1 is ON
        valueStatus=int(cmds.textField(colorTemperature_textBox, query=True, text=True))
        
        # extracting all type of lights from the scene
        areaLights=cmds.ls(type='aiAreaLight')
        skydomeLights=cmds.ls(type='aiSkyDomeLight')
        directionalLights=cmds.ls(type='directionalLight')
        pointLights=cmds.ls(type='pointLight')
        spotLights=cmds.ls(type='spotLight')
        photometricLights=cmds.ls(type='aiPhotometricLight')
        meshLights=cmds.ls(type='aiMeshLight')
        
        
        # connecting all lights of the scene into a single list
        
        all_lights_in_sequence=list(itertools.chain(areaLights, 
                                    skydomeLights, directionalLights,
                                    pointLights, spotLights,
                                    photometricLights, meshLights))
        
        # checking that the list contains all type of lights 
        print(all_lights_in_sequence)
        
        
        # now looping on all  lights to change the color temperature ON or OFF
        # note, the valueStatus is the ON, OFF value. 0 is OFF, 1 is ON
        for light in all_lights_in_sequence:
            
            cmds.setAttr('{}.aiUseColorTemperature'.format(light), valueStatus)
            
            
        
    '''

    .......... UI .............

    '''    



    colorTemperatureTool_window='colorTemperature_tool'


    # checking if the window UI exists

    if cmds.window(colorTemperatureTool_window, exists=True):
        cmds.deleteUI(colorTemperatureTool_window)
        
    else:
        print ('THERE IS NO WINDOW')    

    # FIRST TAB
    # Setting the window variable and naming
    colorTemperatureTool_window = cmds.window('colorTemperature_tool')

    cmds.columnLayout()

    cmds.rowColumnLayout(numberOfColumns=2)

    cmds.text( label='ON/OFF Value', width=200, align= 'center' )
    colorTemperature_textBox = cmds.textField(text='1', width = 40, height = 20)
    cmds.setParent('..')
    cmds.setParent('..')

    cmds.columnLayout()
    cmds.button( label='color temperature switch', command=colorTemperature_switcher, width = 380)

    cmds.setParent('..')
    cmds.setParent('..')



    cmds.showWindow( colorTemperatureTool_window )





