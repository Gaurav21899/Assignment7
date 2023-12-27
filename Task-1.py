import arcpy
import os

x_Delhi = 77.25628601400678
y_Delhi = 28.55938007942285

# Point object
pnt_obj = arcpy.Point(x_Delhi, y_Delhi)

# spatial reference object
spatial_ref = arcpy.SpatialReference("WGS 1984")

#  Point geometry
pnt_geom = arcpy.PointGeometry(pnt_obj, spatial_ref)

gdb_path = r"D:\Programming for GIS-3\Assignment7\Practical_7_ProProject\07_Working_with_Geometry_Objects.gdb"
fc_name = "Delhi"
fc_path = os.path.join(gdb_path, fc_name)

arcpy.CopyFeatures_management(pnt_geom, fc_path)

print("Process Completed")



