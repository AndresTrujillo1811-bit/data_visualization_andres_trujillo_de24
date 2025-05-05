from taipy.gui import Gui
import taipy.gui.builder as tgb

slider_value = 20
selected_fruit = "apple"

with tgb.Page() as page:
    tgb.text("# Hello there Taipy", mode="md")
    tgb.text("Welcome to the world of reactive programming")
    
    tgb.slider(value="{slider_value}", min=1, max=50, step=5)
    tgb.text("Slider value is at {slider_value}")
    tgb.text("Slider value again is at {slider_value}")
    
    tgb.text('Select your favorite fruit', mode="md")
    tgb.selector(value={selected_fruit}, lov=["tomato", "avocado", "banana", "apple"], dropdown=True)
    
    tgb.text("Yummy {selected_fruit}")
    tgb.image("assets/{selected_fruit}.jpg")

if __name__ == '__main__':
    Gui(page).run(dark_mode=False, use_reloader=True, port=8080) 