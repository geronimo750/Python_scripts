# delete first two lines
# setup_for_fluent(product_version="23.1.0", mode="meshing", version="3d", precision="single")
# meshing.execute_tui(r'''(api-start-python-journal "namefile.py")  ''')

#add 4 new lines
import ansys.fluent.core as pyfluent
meshing_session=pyfluent.launch_fluent(precision="double", processor_count=2, mode="meshing", show_gui="true")
workflow=meshing_session.workflow
meshing=meshing_session.meshing
#
workflow.InitializeWorkflow(WorkflowType=r'Watertight Geometry')
meshing.GlobalSettings.LengthUnit.set_state(r'mm')
meshing.GlobalSettings.AreaUnit.set_state(r'mm^2')
meshing.GlobalSettings.VolumeUnit.set_state(r'mm^3')
workflow.TaskObject['Import Geometry'].Arguments.set_state({r'FileName': r'C:/Users/geron-ma/Downloads/PyF_L3_WF/Workshop_files/Input_files/Static Mixer geometry.pmdb',})
workflow.TaskObject['Import Geometry'].Execute()
workflow.TaskObject['Add Local Sizing'].AddChildAndUpdate()
workflow.TaskObject['Generate the Surface Mesh'].Execute()
workflow.TaskObject['Describe Geometry'].UpdateChildTasks(SetupTypeChanged=False)
workflow.TaskObject['Describe Geometry'].Arguments.set_state({r'SetupType': r'The geometry consists of only fluid regions with no voids',})
workflow.TaskObject['Describe Geometry'].UpdateChildTasks(SetupTypeChanged=True)
workflow.TaskObject['Describe Geometry'].Execute()
workflow.TaskObject['Update Boundaries'].Execute()
workflow.TaskObject['Update Regions'].Execute()
workflow.TaskObject['Add Boundary Layers'].Arguments.set_state({r'LocalPrismPreferences': {r'Continuous': r'Stair Step',},})
workflow.TaskObject['Add Boundary Layers'].AddChildAndUpdate()
workflow.TaskObject['Generate the Volume Mesh'].Execute()
# solver.execute_tui(r'''/switch-to-solution-mode yes ''')
# there seem to be a difference between the video and our script
solver = meshing_session.switch_to_solver()
#solver.execute_tui(r'''(newline)  ''')
solver.setup.models.energy = {"enabled" : True}
#THIS WORKS!!!!!!!!!!
#solver.setup.materials.database.copy_by_name(type="fluid", name="water-liquid")

# the execute_tui command does not seem to work anymore
# solver.execute_tui(r'''/define/materials/copy fluid water-liquid ''') 

# suggested by fluent but not working
# solver.tui.define.materials.copy("fluid","water-liquid")

# solver.setup.cell_zone_conditions.fluid['fluid'] = {"material" : "water-liquid"}
# solver.setup.boundary_conditions.velocity_inlet['velocity-inlet-1'].vmag = 1.
# solver.setup.boundary_conditions.velocity_inlet['velocity-inlet-2'].vmag = 1.
# solver.solution.initialization.hybrid_initialize()
# solver.solution.run_calculation.iterate(iter_count = 1000)
# solver.solution.run_calculation.iterate(iter_count = 20)
# solver.exit()

