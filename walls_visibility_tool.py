

wall_geos = [
# List wall groups to check

# Millie's house main groups
'colour:inthousewallfloors_1:geo',
'colour:inthousewallfloors_1:secondFloor_grp',
'colour:inthousewallfloors_1:SF_floor_grp',
'colour:inthousewallfloors_1:SF_ceiling_grp',
'colour:inthousewallfloors_1:MF_floor_grp',
'colour:inthousewallfloors_1:MF_ceiling_grp',

# SECOND FLOOR GROUPS

# Office groups
'colour:inthousewallfloors_1:officeGroup',
'colour:inthousewallfloors_1:OFFICE_wall_Window_grp',
'colour:inthousewallfloors_1:OFFICE_wall_Left_grp',
'colour:inthousewallfloors_1:OFFICE_wall_Right_grp',
'colour:inthousewallfloors_1:OFFICE_wall_Door_grp',

# Girls room
'colour:inthousewallfloors_1:girlsRoomGroup',
'colour:inthousewallfloors_1:GR_wall_window_grp',
'colour:inthousewallfloors_1:GR_wall_Right_grp',
'colour:inthousewallfloors_1:GR_wall_Door_grp',
'colour:inthousewallfloors_1:GR_wall_Left_grp',
'colour:inthousewallfloors_1:GR_floor_grp',

# Hallway second floor
'colour:inthousewallfloors_1:SF_hallway_table_grp',
'colour:inthousewallfloors_1:SF_hallway_walls_grp',
'colour:inthousewallfloors_1:mombedroomGroup',
'colour:inthousewallfloors_1:staircase_grp',
'colour:inthousewallfloors_1:tent_grp',
'colour:inthousewallfloors_1:star_string_grp',

# Mom bedroom
'colour:inthousewallfloors_1:mombedroomGroup',
'colour:inthousewallfloors_1:mombedroom_wall_grp1',
'colour:inthousewallfloors_1:mombedroom_wall_grp2',
'colour:inthousewallfloors_1:mombedroom_wall_grp3',
'colour:inthousewallfloors_1:mombedroom_wall_grp4',
'colour:inthousewallfloors_1:mombedroom_wall_grp5',
'colour:inthousewallfloors_1:mombedroom_wall_grp6',

# bathroom
'colour:inthousewallfloors_1:bathroomGroup',
'colour:inthousewallfloors_1:sfbath_wall_grp1',
'colour:inthousewallfloors_1:sfbath_wall_grp2',
'colour:inthousewallfloors_1:sfbath_wall_grp3',
'colour:inthousewallfloors_1:sfbath_wall_grp4',

# MAIN FLOOR GROUPS

# main groups
'colour:inthousewallfloors_1:MF_ceiling_grp',
'colour:inthousewallfloors_1:MF_floor_grp',

# Hallway main floor
'colour:inthousewallfloors_1:MF_hallway_walls_grp',
'colour:inthousewallfloors_1:entrance_steps_grp',
'colour:inthousewallfloors_1:hw_wall_grp1',
'colour:inthousewallfloors_1:hw_wall_grp2',
'colour:inthousewallfloors_1:hw_wall_grp3',
'colour:inthousewallfloors_1:hw_wall_grp4',
'colour:inthousewallfloors_1:hw_wall_grp5',
'colour:inthousewallfloors_1:hw_wall_grp6',

# livingroom walls
'colour:inthousewallfloors_1:livingroom_walls_grp',
'colour:inthousewallfloors_1:lv_wall_grp1',
'colour:inthousewallfloors_1:lv_wall_grp2',
'colour:inthousewallfloors_1:lv_wall_grp3',
'colour:inthousewallfloors_1:lv_wall_grp4',
'colour:inthousewallfloors_1:fireplace_grp',

# livingroom set dressing
'colour:intlivingroom_1:geo_rig',
'colour:intlivingroom_1:hanging_pot_grp1',
'colour:intlivingroom_1:hanging_pot_grp2',
'colour:intlivingroom_1:logholder_grp',
'colour:intlivingroom_1:ottoman_grp',
'colour:intlivingroom_1:couch_grp',
'colour:intlivingroom_1:armchair_grp',
'colour:intlivingroom_1:floor_lamp_grp',
'colour:intlivingroom_1:dogbed_grp',
'colour:intlivingroom_1:cabinet_grp',

# kitchen groups
'colour:inthousewallfloors_1:kitchen_walls_grp',
'colour:inthousewallfloors_1:kc_wall_grp1',
'colour:inthousewallfloors_1:kc_wall_grp2',
'colour:inthousewallfloors_1:kc_wall_grp3',
'colour:inthousewallfloors_1:kc_wall_grp4',
'colour:inthousewallfloors_1:kc_wall_grp5',
'colour:inthousewallfloors_1:porch_grp'

]


def check_wallGroups_visibility(*args):
    for each_group in wall_geos:
        
        visibility_check = cmds.getAttr('{}.visibility'.format(each_group))
    
        if visibility_check:
            print(each_group+'VISIBILITY_is_ON')
        else:
            cmds.textScrollList(walls_textBox, edit = True, append = each_group)
            print(each_group+'VISIBILITY_is_OFF')
            
def select_OFF_wall(*args):
    selected_group = cmds.textScrollList(walls_textBox, query = True, selectItem=True)[0]
    cmds.select(selected_group)  
    
def query_textScroll_selectedItem(*args):
    selected_group = cmds.textScrollList(walls_textBox, query = True, selectItem=True)[0]
    print (selected_group)
    return (selected_group)
    
    
    
def break_set_visibililty_ON(*args):
    
    selected_group = query_textScroll_selectedItem() 
    print(selected_group)            
    
    
    # Specify the object and attribute
    obj_name = selected_group
    attr_name = "visibility"
    group_visibility_attr = f'{obj_name}.{attr_name}'   
    
    # List connections to the visibility attribute
    visibility_connections = cmds.listConnections(group_visibility_attr, plugs=True)[0]
    
    print(f'THIS IS THE OBJECT CONNECTED TO THE VISIBILITY ATTRIBUTE___{visibility_connections}')
      
    # Disconnect attributes
    print('THIS IS THE COMMAND')
    print(group_visibility_attr+','+visibility_connections)
    cmds.disconnectAttr( visibility_connections, group_visibility_attr )
    
    # Setting visibility ON
    cmds.setAttr(group_visibility_attr, 1)
    
    
def set_visibililty_ON(*args):
    
    selected_group = query_textScroll_selectedItem() 
    print(selected_group)            
    
    
    # Specify the object and attribute
    obj_name = selected_group
    attr_name = "visibility"
    group_visibility_attr = f'{obj_name}.{attr_name}'       
       
    # Setting visibility ON
    cmds.setAttr(group_visibility_attr, 1)
    
    
def remove_all_items_scrollList(*args):
    cmds.textScrollList(walls_textBox, edit = True, removeAll=True)    
                    
                
            
        
#_________________________________________________________

# TOOL  UI 
#_________________________________________________________
        
walls_tool_window='walls_tool'


# checking if the window UI exists

if cmds.window(walls_tool_window, exists=True):
    cmds.deleteUI(walls_tool_window)
    
else:
    print ('THERE IS NO WINDOW')    

# Setting the window variable and naming
walls_tool_window = cmds.window('walls_tool')

# main layout structure and title
cmds.columnLayout()  
cmds.separator(h=10, width = 350)  
cmds.text( label='Check wall groups visiblity', width=350, align= 'center' )

# button to call function that checks visibility 
cmds.separator(h=10, width = 350)
cmds.button( label='Check wall groups visiblity', command = check_wallGroups_visibility, width = 360, height=50)
cmds.separator(h=10, width = 350)


# scroll list for walls with visibility off
cmds.text( label='walls with visibility OFF', width=350, align= 'left')
walls_textBox = cmds.textScrollList(width = 360, selectCommand = select_OFF_wall, height=300)


# button to BREAK and turn visibiility ON
cmds.separator(h=10, width = 350)
cmds.button( label='Break and Switch visibility ON', command = break_set_visibililty_ON, width = 360, height=50)
cmds.separator(h=10, width = 350)


# button to turn visibiility ON ONLY
cmds.separator(h=10, width = 350)
cmds.button( label='Switch visibility ON', command = set_visibililty_ON, width = 360, height=50)
cmds.separator(h=10, width = 350)

# button to CLEAR sccrollList
cmds.separator(h=10, width = 350)
cmds.separator(h=10, width = 350)
cmds.button( label='Refresh', command = remove_all_items_scrollList, width = 360, height=30)
cmds.separator(h=10, width = 350)


cmds.setParent('..')


# show and load window
cmds.showWindow( walls_tool_window )