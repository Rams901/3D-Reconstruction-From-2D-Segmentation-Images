import vtk
reader = vtk.vtkSTLReader()
reader.SetFileName("sample_3d_object.stl")
mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(reader.GetOutputPort())
actor = vtk.vtkActor()
actor.SetMapper(mapper)
renderer = vtk.vtkRenderer()
renderWindow = vtk.vtkRenderWindow()
renderWindow.AddRenderer(renderer)
renderWindowInteractor = vtk.vtkRenderWindowInteractor()
renderWindowInteractor.SetRenderWindow(renderWindow)
renderer.AddActor(actor)
renderer.SetBackground(1, 1, 1) # Background color

# Research on different data set: (different angles): 3D segmentation
# Analyze input for ex2 (pelvis) (.nii )

renderWindow.Render()
renderWindowInteractor.Start()
