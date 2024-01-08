
def layerTool_UI_run():


    import maya.app.renderSetup.model.override as override
    import maya.app.renderSetup.model.selector as selector
    import maya.app.renderSetup.model.collection as collection
    import maya.app.renderSetup.model.renderLayer as renderLayer
    import maya.app.renderSetup.views.overrideUtils as utils
    from maya.app.renderSetup.model.renderSetup import instance
    import mtoa.aovs as aovs
    import maya.cmds as cmds


    # __________ AOVs list __________

    AOV_list =[
    'ID',
    'diffuse',
    'diffuse_indirect',
    'emission',
    'specular',
    'specular_indirect',
    'sss',
    'crypto_asset',
    'crypto_object',
    'RGBA_KEY',
    'RGBA_FILL',
    'RGBA_RIM'
    ]



    def setup_layers_byPrefix(*args):
            
            
        # SETTTING UP LAYERS BY NAMESPACES
        # variables
        exterior = []
        characters = []
        props = []
        
        
        all_world_assets = cmds.ls(assemblies=True)
        
        for item in all_world_assets:
            if item == 'persp':
                all_world_assets.remove(item)
                
        for item in all_world_assets:
            if item == 'top':
                all_world_assets.remove(item)
                    
        for item in all_world_assets:
            if item == 'front':
                all_world_assets.remove(item)
        
        for item in all_world_assets:
            if item == 'side':
                all_world_assets.remove(item)
                
        for item in all_world_assets:
            if item == 'alemSeqSettings':
                all_world_assets.remove(item)
                
        for item in all_world_assets:
            if item == 'CAM:CAM:CAM':
                all_world_assets.remove(item)        
            
        print (all_world_assets)  
        
        
        for item in all_world_assets:
            nameParts = item.split('_')
                    
            
            if 'ext' in item:
                exterior.append(item)
            
            
            if 'ch' in item:
                characters.append(item)            
            
                
            if 'pr' in item:
                props.append(item)  
                
        
        print (exterior)
        print (characters)
        print (props)  
        
        cmds.textScrollList(bg_layer_textBox, edit = True, append=exterior)
        cmds.textScrollList(fg_layer_textBox, edit = True, append=characters)
        cmds.textScrollList(fg_layer_textBox, edit = True, append=props)            
                            
        
    def clearLayers(*args):    
        cmds.textScrollList(bg_layer_textBox, edit = True, removeAll=True)
        cmds.textScrollList(fg_layer_textBox, edit = True, removeAll=True)


    def add_assets_to_BG_textBox(*args):
        BG_selected = cmds.ls(sl=True)
        cmds.textScrollList(bg_layer_textBox, edit = True, append=BG_selected)
        
    def add_assets_to_FG_textBox(*args):
        FG_selected = cmds.ls(sl=True)
        cmds.textScrollList(fg_layer_textBox, edit = True, append=FG_selected)    
        
    def get_BG_objects_from_textBox(*args):
        list_of_BG_assets = cmds.textScrollList(bg_layer_textBox, query = True, allItems = True)    
        print (list_of_BG_assets)
        return list_of_BG_assets
        
    def get_FG_objects_from_textBox(*args):
        list_of_FG_assets = cmds.textScrollList(fg_layer_textBox, query = True, allItems = True)    
        print (list_of_FG_assets)
        return list_of_FG_assets  


        
    # FIRST TAB BG-FG LAYER FUNCTION    
    def create_layer_pass(name, caster_name):
        
        layerName = '{}_pass'.format(name)
        collectionName = '{}_geo'.format(name)    
        geoCasterName = '{}_caster_geo'.format(caster_name)

        rs = instance()

        #this creates a render layer 
        rl = rs.createRenderLayer(layerName)

        # making this new layer as visible
        rs.switchToLayer(rl)
        
        #This creates a lights collection instance inside the created render layer
        l1 = rl.lightsCollectionInstance()

        # create and append collections under the layers    
        c1 = rl.createCollection(collectionName)

        # create and append collections under the layers CASTER   
        c2 = rl.createCollection(geoCasterName)
        
        # adding objects to geo layer collection
        
        if name == 'BG':
        # getting asset list for BG and FG text boxes
            list_of_BG_elements = get_BG_objects_from_textBox() 
            
            BG_expression_list = ''.join(str('|'+item+'* ') for item in list_of_BG_elements)  
                
            c1.getSelector().setPattern(BG_expression_list)
        if name == 'FG':
            
            # getting asset list for BG and FG text boxes
            list_of_FG_elements = get_FG_objects_from_textBox() 
            
            FG_expression_list = ''.join(str('|'+item+'* ') for item in list_of_FG_elements)          
        
            c1.getSelector().setPattern(FG_expression_list)
            
        else:
            print ('NAME IS NEITHER BG OR FG')                           

        # adding objects to CASTER layer collection
        
        if name == 'BG':
        # getting asset list for BG and FG text boxes
            list_of_FG_elements = get_FG_objects_from_textBox()        
            single_FG_group = list_of_FG_elements[0] 
            print ('THIS IS SINGLE FG GROUP')
            print (single_FG_group)
            
            FG_expression_list = ''.join(str('|'+item+'* ') for item in list_of_FG_elements)              
            c2.getSelector().setPattern(FG_expression_list)
            
            # setting a collection for primary visibility OFF
            # create and append collections under the layers CASTER   
            
            c3 = rl.createCollection('PrimaryVisibility OVRD FG')
            c3.getSelector().setPattern('*') 
                        
            #geoShape = get_singleGeo(single_FG_group)  
            allShapes = cmds.listRelatives( single_FG_group, allDescendents=True) 

            for object_FG in allShapes:
                
                if 'Shape' in object_FG:
                    geoToHide_FG = object_FG
                    break 
        
            
            c3.createAbsoluteOverride(geoToHide_FG, 'primaryVisibility')   
            cmds.setAttr('{}.primaryVisibility'.format(geoToHide_FG), 0) 
        
        if name == 'FG':
            # getting asset list for BG and FG text boxes
                list_of_BG_elements = get_BG_objects_from_textBox()        
                single_BG_group = list_of_BG_elements[0] 
                print ('THIS IS SINGLE BG GROUP')
                print (single_BG_group)
                
                BG_expression_list = ''.join(str('|'+item+'* ') for item in list_of_BG_elements)              
                c2.getSelector().setPattern(BG_expression_list)
                
                # setting a collection for primary visibility OFF
                # create and append collections under the layers CASTER   
                
                c3 = rl.createCollection('PrimaryVisibility OVRD BG')
                c3.getSelector().setPattern('*') 
                            
                #geoShape = get_singleGeo(single_FG_group)  
                allShapes = cmds.listRelatives( single_BG_group, allDescendents=True) 
        
                for object_BG in allShapes:
                    
                    if 'Shape' in object_BG:
                        geoToHide_BG = object_BG
                        break 
            
                
                c3.createAbsoluteOverride(geoToHide_BG, 'primaryVisibility')   
                cmds.setAttr('{}.primaryVisibility'.format(geoToHide_BG), 0) 
                
                
                # create aov passes
                for aov in AOV_list: 
        
                    # create light group aov
                    if 'RGBA_' in aov:
                        
                        aovs.AOVInterface().addAOV(aov, aovType='rgba')   
                        
                    else:          
            
                        # Create none light group AOV 
                        aovs.AOVInterface().addAOV(aov, aovType='float')
                            
                    
        else:
            print ('NAME IS NEITHER BG OR FG')      
            
            
            
    def create_passes_wrapper(*args):
        
        create_layer_pass('BG', 'FG')
        create_layer_pass('FG', 'BG')
        
        
                
    #____________________________________________________________________________________________________________________________ 
    
            
    def add_custom_objects_to_A_layer(*args):
        selectedObjects_layerA = cmds.ls(sl=True)
        cmds.textScrollList(layer_A_textBox, edit = True, append = selectedObjects_layerA)
                
    def add_custom_objects_to_B_layer(*args):
        selectedObjects_layerB = cmds.ls(sl=True)
        cmds.textScrollList(layer_B_textBox, edit = True, append = selectedObjects_layerB)   


        
    # SECOND TAB BG-FG LAYER FUNCTION    
    def create_custom_layer_pass(name, caster_name):
        
        layerName = '{}_pass'.format(name)
        collectionName = '{}_geo'.format(name)    
        geoCasterName = '{}_caster_geo'.format(caster_name)

        rs = instance()

        #this creates a render layer 
        rl = rs.createRenderLayer(layerName)

        # making this new layer as visible
        rs.switchToLayer(rl)
        
        #This creates a lights collection instance inside the created render layer
        l1 = rl.lightsCollectionInstance()

        # create and append collections under the layers    
        c1 = rl.createCollection(collectionName)

        # create and append collections under the layers CASTER   
        c2 = rl.createCollection(geoCasterName)
        
        
        
        
        # adding objects to geo layer collection
        # getting asset list for BG and FG text boxes
        list_of_layerA_groups = cmds.textScrollList(layer_A_textBox, query = True, allItems = True) 
        
        layerA_expression_list = ''.join(str('|'+item+'* ') for item in list_of_layerA_groups)  
            
        c1.getSelector().setPattern(layerA_expression_list)
        
        # adding objects to CASTER layer collection
        # getting asset list for BG and FG text boxes
        list_of_layerA_caster_elements = cmds.textScrollList(layer_B_textBox, query = True, allItems = True)        
        single_layerA_caster_geo = list_of_layerA_caster_elements[0] 
        print ('THIS IS SINGLE FG GROUP')
        print (single_layerA_caster_geo)
        
        FG_expression_list = ''.join(str('|'+item+'* ') for item in list_of_layerA_caster_elements)              
        c2.getSelector().setPattern(FG_expression_list)
        
        # setting a collection for primary visibility OFF
        # create and append collections under the layers CASTER   
        
        c3 = rl.createCollection('PrimaryVisibility OVRD FG')
        c3.getSelector().setPattern('*') 
                    
        #geoShape = get_singleGeo(single_layerA_caster_geo)  
        allShapes_layerA = cmds.listRelatives( single_layerA_caster_geo, allDescendents=True) 

        for objects_layerA_caster in allShapes_layerA:
            
            if 'Shape' in objects_layerA_caster:
                geoToHide_layerA_caster = objects_layerA_caster
                break 
    
        
        c3.createAbsoluteOverride(geoToHide_layerA_caster, 'primaryVisibility')   
        cmds.setAttr('{}.primaryVisibility'.format(geoToHide_layerA_caster), 0) 
        
        # create aov passes
        for aov in AOV_list: 

                # create light group aov
                if 'RGBA_' in aov:
                    
                    aovs.AOVInterface().addAOV(aov, aovType='rgba')   
                    
                else:          
        
                    # Create none light group AOV 
                    aovs.AOVInterface().addAOV(aov, aovType='float')
                        

                
                    
    
        
        
        
    def create_custom_passes_wrapper(*args): 

        custom_name = cmds.textField(layerA_name_box, query=True, text=True) 
        
        
        print ('THESE ARE CUSTOM NAME AND CUSSTOM CASTER NAME')
        print (custom_name)    
        create_custom_layer_pass(custom_name, custom_name)  

    
        


            


    #__________________________________________________________________________________________________________________________



    '''
            UI ............................................................

        LAYER TOOL WITH TABS

    - Reanmes a list of selected objects based on string attributes.
    - This predefined attributes are editable in the UI.
    - It evaluates each item in the selection to see if is a "group" or a "geo" and renames it with the proper suffix.
    _____________________________________________________________________________________________________________


    SCRIPT TO LOAD THIS MODULE (TO BE RUN IN MAYA)
    NOTE: I need to add the custom path because I use OneDrive. This resolves maya to no been able to see the documents
    folder. Thus, it can not find the scripts folder and it fails to load the module.
    The path has to be appended to maya paths.
    _____________________________________________________________________________________________________________

    import maya.cmds as cmds
    import importlib

    import sys
    sys.path.append('C:/Users/agust/OneDrive/01_TINTO/DOCUMENTS/GitHub/rename_tool')

    import rename_tool
    importlib.reload(rename_tool)

    rename_tool

    '''

    import maya.cmds as cmds


    '''
    --------------------------------------window ui------------------------------------------
    Note: The tool is setup by stacking different types of layouts bellow each other.
    All layouts live under a main column layout (the first one after the creation of the window)
    The cmds.setParent('..')  line parents each layout bellow the main columnlayout. This is needed so each control
    or widget is placed in the proper layout as desired. If not, the next widget will be parented based 
    on the previous layout
    -----------------------------------------------------------------------------------------------
    '''
    layerTool_window='layer_tool'


    # checking if the window UI exists

    if cmds.window(layerTool_window, exists=True):
        cmds.deleteUI(layerTool_window)
        
    else:
        print ('THERE IS NO WINDOW')    

    # FIRST TAB
    # Setting the window variable and naming
    layerTool_window = cmds.window('layer_tool')

    cmds.paneLayout()
    tabs = cmds.tabLayout(innerMarginWidth=5, innerMarginHeight=5)
    main_layers = cmds.columnLayout()

    cmds.separator(h=10, width = 350)
    cmds.button( label='create layers by prefix', command = setup_layers_byPrefix, width = 150)
    cmds.separator(h=10, width = 350)

    cmds.text( label='BG_layer', width=350, align= 'center' )
    cmds.rowColumnLayout( numberOfColumns=2, columnAttach=(1, 'right', 0), columnWidth=[(1, 100), (2, 250)] )
    bg_layer_textBox = cmds.textScrollList(width = 360, height = 100)
    cmds.setParent('..')


    cmds.columnLayout()
    cmds.text( label='FG_layer', width=350, align= 'center' )
    fg_layer_textBox = cmds.textScrollList(width = 360, height = 100)
    cmds.setParent('..')



    cmds.rowColumnLayout(numberOfColumns=2)
    cmds.button( label='Add BG groups', command = add_assets_to_BG_textBox, width = 175)
    cmds.button( label='Add FG groups', command = add_assets_to_FG_textBox, width = 175)
    cmds.setParent('..')


    # create layer button
    cmds.separator(h=30, width = 350)
    cmds.button( label='Create Layers', command = create_passes_wrapper, width = 350)
    cmds.separator(h=30, width = 350)
    cmds.button( label='clear layers', command = clearLayers, width = 350)


    cmds.separator(h=10, width = 350)
    cmds.text( label='custom AOVs list', width=350, align= 'center' )

    AOVs_textBox = cmds.textScrollList(append = AOV_list, width = 360, height = 100)


    cmds.setParent('..')


    # SECOND TAB
    # Setting the window variable and naming


    custom_layers = cmds.paneLayout()

    cmds.columnLayout()

    cmds.text( label='Custom Layer A Name' )
    layerA_name_box = cmds.textField(text = 'layer_A' ,width = 350)
    cmds.separator(h=10, width = 350)


    cmds.text( label='custom_LAYER_A', width=350, align= 'center' )
    cmds.rowColumnLayout( numberOfColumns=2, columnAttach=(1, 'right', 0), columnWidth=[(1, 100), (2, 250)] )
    layer_A_textBox = cmds.textScrollList(width = 360, height = 100)
    cmds.setParent('..')


    cmds.columnLayout()
    cmds.text( label='custom_LAYER_A_CASTER', width=350, align= 'center' )
    layer_B_textBox = cmds.textScrollList(width = 360, height = 100)
    cmds.setParent('..')


    cmds.rowColumnLayout(numberOfColumns=2)
    cmds.button( label='Add CUSTOM LAYER A groups', command = add_custom_objects_to_A_layer, width = 175)
    cmds.button( label='Add CUSTOM LAYER A casters', command = add_custom_objects_to_B_layer, width = 175)
    cmds.setParent('..')


    # create layer button
    cmds.separator(h=30, width = 350)
    cmds.button( label='Create custom Layers', command = create_custom_passes_wrapper, width = 350)
    cmds.separator(h=30, width = 350)
    cmds.button( label='clear custom layers', command = clearLayers, width = 350)

    cmds.separator(h=10, width = 350)
    cmds.text( label='custom AOVs list', width=350, align= 'center' )
    cmds.separator(h=10, width = 350)

    AOVs_textBox = cmds.textScrollList(append = AOV_list, width = 360, height = 100)
    cmds.setParent('..')



    # parenting tabs
    cmds.tabLayout( tabs, edit=True, tabLabel=((main_layers, 'main_layers'), (custom_layers, 'custom_layers')))


    cmds.showWindow( layerTool_window )
