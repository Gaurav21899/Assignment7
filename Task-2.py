import arcpy
import os

gdb_path = r"D:\Programming for GIS-3\Assignment7\Practical_7_ProProject\07_Working_with_Geometry_Objects.gdb"
output_fc_name = "Mumbai_to_Pune"
output_fc_path = os.path.join(gdb_path, output_fc_name)

x_mum = 72.8219812049458
y_mum = 19.213629059616597

x_pune = 73.8509482530976
y_pune = 18.453407357784993

pnt_mumbai_obj = arcpy.Point(x_mum, y_mum)
pnt_pune_obj = arcpy.Point(x_pune, y_pune)
# Spatial Reference object
spatial_ref = arcpy.SpatialReference("WGS 1984")
#Array object
polyline_array = arcpy.Array()

polyline_array.add(pnt_mumbai_obj)
polyline_array.add(pnt_pune_obj)

polyline_geom = arcpy.Polyline(polyline_array, spatial_ref)

arcpy.CopyFeatures_management(polyline_geom, output_fc_path)

print("Process completed")

