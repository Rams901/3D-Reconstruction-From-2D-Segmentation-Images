import vtk
import argparse

def main(stl_file):
    # Read the STL file
    reader = vtk.vtkSTLReader()
    reader.SetFileName(stl_file)

    # Map the data
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(reader.GetOutputPort())

    # Create an actor
    actor = vtk.vtkActor()
    actor.SetMapper(mapper)

    # Create a renderer
    renderer = vtk.vtkRenderer()

    # Create a render window
    renderWindow = vtk.vtkRenderWindow()
    renderWindow.AddRenderer(renderer)

    # Create a render window interactor
    renderWindowInteractor = vtk.vtkRenderWindowInteractor()
    renderWindowInteractor.SetRenderWindow(renderWindow)

    # Add actor to the renderer
    renderer.AddActor(actor)
    renderer.SetBackground(1, 1, 1) # Background color

    # Render and interact
    renderWindow.Render()
    renderWindowInteractor.Start()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Visualize a 3D object from an STL file.")
    parser.add_argument('--file', type=str, default='assets/full_lungs.stl', 
                        help="Path to the .stl file (default: 'assets/full_lungs.stl')")
    args = parser.parse_args()
    
    main(args.file)