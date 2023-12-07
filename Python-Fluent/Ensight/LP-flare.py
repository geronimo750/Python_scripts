windvelocity="3ms"
print("wind velocity is " + windvelocity)

#watermark off
ensight.view.watermark("OFF")
#hide components that are not the flare
ensight.part.select_begin(1,7,8,9,10,11,12,13,14,15,16,17,18,19)
ensight.part.visible("OFF")
ensight.part.select_begin(2,3,4,5,6)
ensight.part.colorby_palette("none")
ensight.part.colorby_rgb(0.8,0.8,0.8)

#Part starting extracting results
ensight.part.select_begin(1)
ensight.clip.begin()
ensight.clip.mesh_plane("X")
ensight.clip.value("MID-RANGE")
ensight.clip.tool("xyz")
ensight.clip.slider_x(-50,50)
ensight.clip.slider_y(-50,200)
ensight.clip.slider_z(-50.9399986,199.059998)
ensight.clip.slider_step(5)
ensight.clip.end()
ensight.clip.create()
ensight.part.select_begin(20)

# turn view perpendicular to x axis
ensight.view_transf.view_from_triad_axis("+x")
#view
ensight.part.select_begin(20)
ensight.part.visible("ON")
#this needs to be adjusted according to the domain and the zoom required
#Cold  flare
ensight.view_transf.look_at(0,65,75)
ensight.view_transf.look_from(0,65,360)
#Sandy warm flare
#ensight.view_transf.look_at(128,38,174)
#ensight.view_transf.look_from(128,38,348)
#LP flare
#ensight.view_transf.look_at(66,7,74)
#ensight.view_transf.look_from(66,7,113)
#
#ensight.view_transf.center_of_transform(0,75,75)
#ensight.view_transf.zclip_front(34.8149109)
ensight.tools.select_tool("OFF")
ensight.annotation.axis_model("OFF")

# writing part
ensight.text.rgb(1,1,1)
ensight.text.new_text("Wind")
ensight.text.select_begin(0)
ensight.text.visible("OFF")
#ensight.text.location_x(0.9)
#ensight.text.location_y(0.9)

#
ensight.line.select_default()
ensight.line.label_text_id(0)
ensight.line.new_line()
ensight.line.select_begin(0)
ensight.line.rgb(1,1,1)
ensight.line.width(3)
ensight.line.arrowhead("on_second_end")
ensight.line.location_x_1(0.95)
ensight.line.location_y_1(0.9)
ensight.line.location_x_2(0.8)
ensight.line.location_y_2(0.9)

ensight.text.new_text("HP tip")
ensight.text.select_begin(1)
ensight.text.size(40)
ensight.text.visible("OFF")

ensight.line.select_default()
ensight.line.label_text_id(1)
ensight.line.new_line()
ensight.line.select_begin(1)
ensight.line.rgb(1,1,1)
ensight.line.arrowhead("on_second_end")
ensight.line.width(3)
ensight.line.location_x_1(0.91)
ensight.line.location_y_1(0.14)
ensight.line.location_x_2(0.82)
ensight.line.location_y_2(0.14)





#put temperature as variable
ensight.legend.select_palette_begin("temperature")
ensight.legend.visible("ON")
ensight.part.select_begin(20)
ensight.variables.activate("temperature")
ensight.part.modify_begin()
ensight.part.colorby_palette("temperature")
ensight.part.modify_end()
ensight.legend.select_palette_begin("temperature")
ensight.legend.visible("OFF")
# #define range and change palette
ensight.function.palette("temperature")
ensight.function.range(300,2200)
ensight.function.modify_begin()
ensight.function.restore_predefinedpal("use_new_levels","2hot")
ensight.function.modify_end()
#export image temperature
ensight.file.image_rend_offscreen("ON")
ensight.file.image_numpasses(4)
ensight.file.image_stereo("current")
ensight.file.image_screen_tiling(1,1)
ensight.file.image_format_options("Compression Default")
ensight.file.image_file(r"""C:\Users\geron-ma\OneDrive - TUV SUD\Temp\PPP\fig-temp-"""+windvelocity)
ensight.file.image_window_size("normal")
#ensight.file.image_window_xy(1280,985)
ensight.file.image_raytrace_it("ON")
ensight.file.save_image()
#
# --------------------O2------------------------

#remove vision of the flare
ensight.part.select_begin(2,3,4,5,6)
ensight.part.visible("OFF")
#put o2 as variable 
ensight.legend.select_palette_begin("o2")
ensight.legend.visible("OFF")
ensight.part.select_begin(20)
ensight.variables.activate("o2")
ensight.part.modify_begin()
ensight.part.colorby_palette("o2")
ensight.part.modify_end()
ensight.legend.select_palette_begin("o2")
ensight.legend.visible("OFF")
# #define range and change palette
ensight.function.palette("o2")
ensight.function.range(0.0,0.23)
ensight.function.modify_begin()
ensight.function.restore_predefinedpal("use_new_levels","BD_Spectral_11")
ensight.function.modify_end()
#export image temperature
var="o2"
ensight.file.image_rend_offscreen("ON")
ensight.file.image_numpasses(4)
ensight.file.image_stereo("current")
ensight.file.image_screen_tiling(1,1)
ensight.file.image_format_options("Compression Default")
ensight.file.image_file(r"""C:\Users\geron-ma\OneDrive - TUV SUD\Temp\PPP\fig-"""+var+"-"+windvelocity)
ensight.file.image_window_size("normal")
#ensight.file.image_window_xy(1280,985)
ensight.file.image_raytrace_it("ON")
ensight.file.save_image()