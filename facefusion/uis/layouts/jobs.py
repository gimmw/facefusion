import gradio

from facefusion import state_manager
from facefusion.uis.components import about, job_list, job_list_options


def pre_check() -> bool:
	return True


def render() -> gradio.Blocks:
	with gradio.Blocks() as layout:
		with gradio.Row():
			with gradio.Column(scale = 4):
				with gradio.Blocks():
					about.render()
				with gradio.Blocks():
					job_list_options.render()
			with gradio.Column(scale = 11):
				with gradio.Blocks():
					job_list.render()
	return layout


def listen() -> None:
	job_list_options.listen()
	job_list.listen()


def run(ui : gradio.Blocks) -> None:  
    root_path = state_manager.get_item('root_path')  
    launch_kwargs = {  
        'favicon_path': 'facefusion.ico',  
        'inbrowser': state_manager.get_item('open_browser')  
    }  
    if root_path:  
        launch_kwargs['app_kwargs'] = {'root_path': root_path}  
    ui.launch(**launch_kwargs)
