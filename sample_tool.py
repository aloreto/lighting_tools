
def samplesTool_UI_run():


    import os
    import json
    import maya.cmds as cmds

    # 'r' means 'raw'. This means that words like '\n' or '\t'
    # which are built in functions of python will not be erroing by reading a path. 

    dir_path=r'Z:\users\arodriguez\scripts'
    print(dir_path)

    renderSettings_file='renderSettings_profiles.json'
    print(renderSettings_file)

    full_path=os.path.join(dir_path, renderSettings_file)
    print(full_path)


    def read_render_settings_json(file_path):
        with open(file_path, 'r') as f:
            renderSettings_dictionary = json.load(f)
            
        return renderSettings_dictionary   
        
    # reading settings from json file
    renderSettings_dictionary = read_render_settings_json(full_path)
    print (renderSettings_dictionary) 

    lgt_content_dict=renderSettings_dictionary['lgt_content']   
    lgt_beauty_dict=renderSettings_dictionary['lgt_beauty'] 
    lgt_lowRes_dict=renderSettings_dictionary['lgt_lowRes']         

                            
    # for loop to set each dictionary variable.                         


    def lgt_profile_function(profile):
        
        for sample_setting, value in profile.items():
            cmds.setAttr('defaultArnoldRenderOptions.{}'.format(sample_setting), value)    
        
        
    


    def set_lgt_beauty(*args):   
        
        cmds.textScrollList(samples_text,edit = True, removeAll=True)    
    
        for sample_setting, value in lgt_beauty_dict.items():
            cmds.textScrollList(samples_text,edit = True, append='{},{}'.format(sample_setting, value) )   

        lgt_profile_function(lgt_beauty_dict)   


    def set_lgt_content(*args):
        
        
        cmds.textScrollList(samples_text,edit = True, removeAll=True)
        
        for sample_setting, value in lgt_content_dict.items():
            cmds.textScrollList(samples_text,edit = True, append='{},{}'.format(sample_setting, value) )     

        lgt_profile_function(lgt_content_dict) 
        
        
        
    def set_lgt_lowRes(*args):
        
        
        cmds.textScrollList(samples_text,edit = True, removeAll=True)
        
        for sample_setting, value in lgt_lowRes_dict.items():
            cmds.textScrollList(samples_text,edit = True, append='{},{}'.format(sample_setting, value) )     

        lgt_profile_function(lgt_lowRes_dict)     
        
        
    # load samples in text functions

    def load_lgt_beauty(*args):   
        
        cmds.textScrollList(samples_text,edit = True, removeAll=True)    
    
        for sample_setting, value in lgt_beauty_dict.items():
            cmds.textScrollList(samples_text,edit = True, append='{},{}'.format(sample_setting, value) )   




    def load_lgt_content(*args):
        
        
        cmds.textScrollList(samples_text,edit = True, removeAll=True)
        
        for sample_setting, value in lgt_content_dict.items():
            cmds.textScrollList(samples_text,edit = True, append='{},{}'.format(sample_setting, value) )     


        
        
        
    def load_lgt_lowRes(*args):
        
        
        cmds.textScrollList(samples_text,edit = True, removeAll=True)
        
        for sample_setting, value in lgt_lowRes_dict.items():
            cmds.textScrollList(samples_text,edit = True, append='{},{}'.format(sample_setting, value) )     


            
        



    #-----------------------------------------------------------------------------------------

    samplesTool_window='samples_tool'


    # checking if the window UI exists

    if cmds.window(samplesTool_window, exists=True):
        cmds.deleteUI(samplesTool_window)
        
    else:
        print ('THERE IS NO WINDOW')    

    # FIRST TAB# Setting the window variable and naming
    samplesTool_window = cmds.window('samples_tool')

    cmds.columnLayout()

    itemsList = cmds.rowColumnLayout(numberOfColumns=3)

    # title
    cmds.separator(h=20, width = 100)
    cmds.text( label='sample profile selection', width=150, align= 'center' )
    cmds.separator(h=20, width = 100)

    # lgt_beauty
    cmds.text( label='lgt_beauty', width=50, align= 'center' )
    cmds.button( label='set', width = 100, command = set_lgt_beauty)
    cmds.button( label='load', width = 100, command = load_lgt_beauty)
    cmds.separator(h=20, width = 100)
    cmds.separator(h=20, width = 100)
    cmds.separator(h=20, width = 100)

    # lgt_content
    cmds.text( label='lgt_content', width=50, align= 'center')
    cmds.button( label='set', width = 100, command = set_lgt_content )
    cmds.button( label='load', width = 100, command = load_lgt_content)
    cmds.separator(h=20, width = 100)
    cmds.separator(h=20, width = 100)
    cmds.separator(h=20, width = 100)

    # lgt_lowRes
    cmds.text( label='lgt_lowRes', width=50, align= 'center' )
    cmds.button( label='set', width = 100, command = set_lgt_lowRes)
    cmds.button( label='load', width = 100, command = load_lgt_lowRes)
    cmds.separator(h=20, width = 100)
    cmds.separator(h=20, width = 100)
    cmds.separator(h=20, width = 100)

    cmds.setParent('..')




    cmds.columnLayout()
    samples_text=cmds.textScrollList(h=250, w=350)
    cmds.setParent('..')

    cmds.showWindow( samplesTool_window )
        
        

