windvelocity="12ms"
print("wind velocity is " + windvelocity)

#watermark off
view: watermark OFF
#hide components that are not the flare
ensight.part.select_begin(7,8,9,10,11,12,13,14,15,16,17,18,19)
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
ensight.view_transf.look_at(-5,65,75)
ensight.view_transf.look_from(-5,65,360)
ensight.view_transf.center_of_transform(0,75,75)
ensight.view_transf.zclip_front(34.8149109)
ensight.tools.select_tool("OFF")
ensight.annotation.axis_model("OFF")
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
ensight.file.image_file(r"""C:\Users\geron-ma\Pictures\fig-temp"""+windvelocity)
ensight.file.image_window_size("user_defined")
ensight.file.image_window_xy(1280,985)
ensight.file.save_image()
#
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
ensight.function.range(0.0,0.21)
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
ensight.file.image_file(r"""C:\Users\geron-ma\Pictures\fig-"""+var+windvelocity)
ensight.file.image_window_size("user_defined")
ensight.file.image_window_xy(1280,985)
ensight.file.save_image()